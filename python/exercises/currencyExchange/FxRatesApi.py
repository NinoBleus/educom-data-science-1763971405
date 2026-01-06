import http.client
from dotenv import load_dotenv
import os, json, datetime

# Load env variables
load_dotenv()

# Defines
FILE_PATH_FOLDER_NAME= "./jsonCaches/"
FILE_PATH_CURRENCIES = "./jsonCaches/currencies.json"


# Begin FxRateApi Functions

def get_currencies() -> bytes:
    conn = http.client.HTTPSConnection("api.fxratesapi.com")
    
    conn.request("GET", f"/currencies")

    res = conn.getresponse()    
    data = res.read()

    return data
    
def get_exchange_rate(currencies: str, base: str = "EUR", format: str = "json") -> bytes:
    api_key = os.getenv("FxRateApi_key")
    conn = http.client.HTTPSConnection("api.fxratesapi.com")

    query = f"/latest?api_key={api_key}&base={base}"
    if currencies:
        query += f"&currencies={currencies}"
    if format:
        query += f"&format={format}"
    conn.request("GET", query)

    res = conn.getresponse()
    data = res.read()

    return data
    
# End FxRateApi Functions
    
    
    
# Begin Json Functions

def write_json(file_path: str, items: dict | list) -> bool:
    try:
        with open(file_path, mode='w') as json_file:
            json.dump(items, json_file, indent=2)
        return True
    except OSError as e:
        print('Failed to write to json file: ', e)

    return False


def read_json(file_path: str) -> dict | list:

    try:
        with open(file_path, mode='r') as json_file:
            data = json.load(json_file)
        return data
    except OSError as e:
        print('Failed to read from json file: ', e)
    except json.JSONDecodeError as e:
        print('Failed to decode json file: ', e)

    return []


def check_file_exist(file_path: str) -> bool:
    if os.path.exists(file_path):
        return True
    else:
        return False

    
def check_modified_within_time(file_path: str, hours: int = 1) -> bool:
    required_time = datetime.datetime.now() - datetime.timedelta(hours = hours)
    last_modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
    if last_modified_time >= required_time:
        return True
    else:
        return False

# End Json Functions



# Begin Business Logic

def show_all_currencies(file_path: str = FILE_PATH_CURRENCIES) -> dict | list:
    if check_file_exist(file_path) and check_modified_within_time(file_path, 168): # 168 hours = 1 week
        currencies = read_json(file_path)
        # print(currencies)
        return currencies
    else:
        currencies_bytes = get_currencies()
        currencies_data = json.loads(currencies_bytes)
        write_json(FILE_PATH_CURRENCIES, currencies_data)
        cached_currencies = read_json(file_path)
        # print(cached_currencies)
        return cached_currencies
            
def show_currency_rates(currencies: str, base: str = "EUR", format: str = "json") -> dict | list:
    if currencies != "":
        file_path_name = FILE_PATH_FOLDER_NAME+f"{base}_To_{currencies}_Currency_rate.json"
    else: 
        file_path_name = FILE_PATH_FOLDER_NAME+f"{base}_To_All_Currency_rate.json"

    if check_file_exist(file_path_name) and check_modified_within_time(file_path_name, 1):
        currency_rates = read_json(file_path_name)
        # print(currency_rates)
        return currency_rates
    else:
        currencies_rates_bytes = get_exchange_rate(currencies=currencies, base=base, format=format)
        currencies_rates_data = json.loads(currencies_rates_bytes)
        write_json(file_path_name, currencies_rates_data)
        cached_currencies_rates = read_json(file_path_name)
        # print(cached_currencies_rates)
        return cached_currencies_rates
        
# End Business Logic



# Begin main

def main():
    options = show_all_currencies()
    while True:
        print("Select base currency: (type help to show all possible currencies)")
        user_input = input().strip().upper()
        if user_input == "HELP":
            options = show_all_currencies()
            for code, info in options.items():
                print(f"{code} - {info.get('name', '')}")
            continue
        if user_input in options:
            print("Select currencies to convert base currency to: (leave empty to get all)")
            print("Format should be as follows: EUR,BTC,GBP")
            currencies = input().strip().upper().replace(" ", "")
            rates = show_currency_rates(base=user_input, currencies=currencies)
            print(json.dumps(rates, indent=2))

        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()

# End main
