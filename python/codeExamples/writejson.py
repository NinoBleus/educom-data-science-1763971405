from json import dump
import sys
from dataclasses import dataclass


@dataclass
class Person:
    id: int
    name: str
    age: int
    city: str


def write_json(file_path: str, items: list) -> bool:
    try:
        with open(file_path, mode='w') as json_file:
            dump(items, json_file, indent=2)
        return True
    except OSError as e:
        print('Failed to write to json file: ', e)

    return False


def get_path() -> str:
    try:
        return sys.argv[1]
    except IndexError:
        return ''
    

def get_content() -> str:
    try:
        return sys.argv[2:]
    except IndexError:
        return ''


def string_to_object(inputString) -> list[Person]:
    persons: list[Person] = []
    for i in range(0, len(inputString), 4):
        persons.append(
            Person(
                id = int(inputString[i]),
                name = inputString[i + 1],
                age = int(inputString[i + 2]),
                city = inputString[i + 3],
            )
        )
    return persons


def object_to_json(inputObject: list[Person]):
    return [
        {"Id": person.id, "Name": person.name, "Age": person.age, "City": person.city}
        for person in inputObject
    ]
     


def main():
    path = get_path()
    content = get_content()
    json = object_to_json(string_to_object(content))
    succes = write_json(path, json)
    if succes:
        print('Succesfully wrote text to json')
    else:
        print("Couldn't write text to file")
    

if __name__ == "__main__":
    main()
