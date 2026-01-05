from .db import get_connection

def create_or_update(table: str, data: dict, row_id: int | None = None) -> tuple[int, bool]:
    conn = get_connection()
    cur = conn.cursor()
    record_id = row_id if row_id is not None else data.get("id")

    try:
        if record_id is not None:
            cur.execute(f"SELECT 1 FROM {table} WHERE id=%s", (record_id,))
            exists = cur.fetchone() is not None
        else:
            exists = False

        if exists:
            update_data = {key: value for key, value in data.items() if key != "id"}
            if update_data:
                set_clause = ", ".join([f"{key}=%s" for key in update_data.keys()])
                query = f"UPDATE {table} SET {set_clause} WHERE id=%s"
                values = list(update_data.values()) + [record_id]
                cur.execute(query, values)
                conn.commit()
            return record_id, cur.rowcount > 0

        insert_data = dict(data)
        if insert_data.get("id") is None:
            insert_data.pop("id", None)
        if not insert_data:
            raise ValueError("No data to insert.")
        columns = ", ".join(insert_data.keys())
        placeholders = ", ".join(["%s"] * len(insert_data))
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        values = list(insert_data.values())

        cur.execute(query, values)
        conn.commit()
        return cur.lastrowid or record_id or 0, True
    finally:
        cur.close()
        conn.close()

def read_one(table: str, row_id: int) -> dict | None:
    query = f"SELECT * FROM {table} WHERE id=%s"
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute(query, (row_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row

def read_all(table: str) -> list[dict]:
    query = f"SELECT * FROM {table}"
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows


def delete(table: str, row_id: int) -> int:
    query = f"DELETE FROM {table} WHERE id=%s"
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(query, (row_id,))
    conn.commit()
    changed = cur.rowcount
    cur.close()
    conn.close()
    return changed
