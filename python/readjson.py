from json import load, JSONDecodeError
import sys
from dataclasses import dataclass

@dataclass
class Person:
    id: int
    name: str
    age: int
    city: str

def read_json(file_path: str) -> list:

    try:
        with open(file_path, mode='r') as json_file:
            data = load(json_file)
        return data
    except OSError as e:
        print('Failed to read from json file: ', e)
    except JSONDecodeError as e:
        print('Failed to decode json file: ', e)

    return []

# def json_to_object():



def main():
    args = sys.argv[1:]
    if len(args) <= 0:
        print('Usage: python readjson.py <path to file>')
    
    path = args[0]
    succes = read_json(path)
    if succes:
        print('Succesfully read text from json')
    else:
        print("Couldn't read text from file")


if __name__ == "__main__":
    main()
