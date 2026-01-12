import argparse
import datetime as dt
import os
import sys
from typing import Dict, List, Optional, Tuple

import matplotlib.dates as mdates
import matplotlib.pyplot as plt

try:
    import duckdb
except ImportError: 
    print("Missing dependency: duckdb. Install with `python3 -m pip install duckdb`.", file=sys.stderr)
    raise SystemExit(1)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_DB_PATH = os.path.join(BASE_DIR, "fxrates.duckdb")


def _parse_rate_datetime(value: object) -> Optional[dt.datetime]:
    text = str(value).strip()
    if not text:
        return None
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    try:
        parsed = dt.datetime.fromisoformat(text)
    except ValueError:
        try:
            parsed = dt.datetime.fromisoformat(f"{text}T00:00:00")
        except ValueError:
            return None
    if parsed.tzinfo:
        parsed = parsed.astimezone(dt.timezone.utc).replace(tzinfo=None)
    return parsed


def _bucket_datetime(value: dt.datetime, bucket: str) -> dt.datetime:
    if bucket == "hour":
        return value.replace(minute=0, second=0, microsecond=0)
    if bucket == "day":
        return value.replace(hour=0, minute=0, second=0, microsecond=0)
    if bucket == "month":
        return value.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    if bucket == "year":
        return value.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
    return value


def _infer_bucket(
    dates: List[dt.datetime],
    start_date: Optional[dt.date],
    end_date: Optional[dt.date],
) -> str:
    if start_date and end_date:
        start_dt = dt.datetime.combine(start_date, dt.time.min)
        end_dt = dt.datetime.combine(end_date, dt.time.max)
        span = end_dt - start_dt
    elif dates:
        span = max(dates) - min(dates)
    else:
        return "day"

    span_days = span.total_seconds() / 86400
    if span_days <= 2:
        return "hour"
    if span_days <= 120:
        return "day"
    if span_days <= 365 * 5:
        return "month"
    return "year"


def load_rates(
    db_path: str,
    base: str,
    currency: str,
    start_date: Optional[dt.date],
    end_date: Optional[dt.date],
) -> Tuple[List[dt.datetime], List[float]]:
    query = (
        """
        select rate_date, rate, fetched_at
        from fx_rates
        where base = ? and currency = ?
        """
    )
    params: List[object] = [base, currency]
    if start_date:
        query += " and substr(rate_date, 1, 10) >= ?"
        params.append(start_date.isoformat())
    if end_date:
        query += " and substr(rate_date, 1, 10) <= ?"
        params.append(end_date.isoformat())
    query += " order by fetched_at"

    with duckdb.connect(db_path, read_only=True) as con:
        rows = con.execute(query, params).fetchall()

    parsed_rows: List[Tuple[dt.datetime, float]] = []
    parsed_dates: List[dt.datetime] = []
    for rate_date, rate, _fetched_at in rows:
        parsed_date = _parse_rate_datetime(rate_date)
        if not parsed_date:
            continue
        parsed_rows.append((parsed_date, float(rate)))
        parsed_dates.append(parsed_date)

    if not parsed_rows:
        return [], []

    bucket = _infer_bucket(parsed_dates, start_date, end_date)
    totals_by_bucket: Dict[dt.datetime, float] = {}
    counts_by_bucket: Dict[dt.datetime, int] = {}

    for parsed_date, rate_value in parsed_rows:
        bucket_date = _bucket_datetime(parsed_date, bucket)
        totals_by_bucket[bucket_date] = totals_by_bucket.get(bucket_date, 0.0) + rate_value
        counts_by_bucket[bucket_date] = counts_by_bucket.get(bucket_date, 0) + 1

    dates = sorted(totals_by_bucket)
    rates = [totals_by_bucket[date] / counts_by_bucket[date] for date in dates]
    return dates, rates


def plot_rates(
    dates: List[dt.datetime],
    rates: List[float],
    base: str,
    currency: str,
    output_path: Optional[str],
    start_date: Optional[dt.date],
    end_date: Optional[dt.date],
) -> None:
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.plot(dates, rates, marker="o", linewidth=1.5)
    ax.set_title(f"{base}/{currency} exchange rate")
    ax.set_xlabel("Date")
    ax.set_ylabel("Rate")
    ax.grid(True, alpha=0.3)

    if start_date or end_date:
        xmin = dt.datetime.combine(start_date, dt.time.min) if start_date else min(dates)
        xmax = dt.datetime.combine(end_date, dt.time.max) if end_date else max(dates)
        if xmin == xmax:
            xmax = xmin + dt.timedelta(days=1)
        ax.set_xlim(xmin, xmax)
    elif dates:
        xmin, xmax = min(dates), max(dates)
        if xmin == xmax:
            pad = dt.timedelta(hours=6)
            ax.set_xlim(xmin - pad, xmax + pad)

    locator = mdates.AutoDateLocator(minticks=4, maxticks=10)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(locator))
    fig.autofmt_xdate()

    if output_path:
        fig.savefig(output_path, dpi=150, bbox_inches="tight")
    else:
        plt.show()

    plt.close(fig)


def _parse_date_arg(value: str) -> dt.date:
    try:
        return dt.date.fromisoformat(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("Date must be in YYYY-MM-DD format.") from exc


def main() -> int:
    parser = argparse.ArgumentParser(description="Plot FX rates from the DuckDB database.")
    parser.add_argument("--db", default=DEFAULT_DB_PATH, help="Path to the fxrates.duckdb file.")
    parser.add_argument("--base", default="EUR", help="Base currency (default: EUR).")
    parser.add_argument("--currency", required=True, help="Quoted currency to plot (e.g. USD).")
    parser.add_argument("--start-date", type=_parse_date_arg, help="Filter from date (YYYY-MM-DD).")
    parser.add_argument("--end-date", type=_parse_date_arg, help="Filter to date (YYYY-MM-DD).")
    parser.add_argument("--out", default="fx_rates.png", help="Output image path.")
    parser.add_argument("--show", action="store_true", help="Show the plot instead of saving it.")
    args = parser.parse_args()

    if not os.path.exists(args.db):
        print(f"Database file not found: {args.db}", file=sys.stderr)
        return 1

    if args.start_date and args.end_date and args.start_date > args.end_date:
        print("Start date must be before or equal to end date.", file=sys.stderr)
        return 1

    dates, rates = load_rates(
        args.db,
        args.base.upper(),
        args.currency.upper(),
        args.start_date,
        args.end_date,
    )
    if not dates:
        print(f"No rates found for {args.base}/{args.currency}.", file=sys.stderr)
        return 1

    output_path = None if args.show else args.out
    plot_rates(
        dates,
        rates,
        args.base.upper(),
        args.currency.upper(),
        output_path,
        args.start_date,
        args.end_date,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
