import json
import csv
import sys
import xml.etree.ElementTree as ElementTree
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Person:
    id: int
    name: str
    age: int
    city: str


def get_extension(file_path) -> str:
    ext = Path(file_path).suffix

    return ext


def get_path() -> str:
    try:
        return sys.argv[1]
    except IndexError:
        print("Path doesn't exist or is wrong.")


def to_person(person_id, name, age, city) -> Person:
    return Person(
        id=int(person_id),
        name=name,
        age=int(age),
        city=city,
    )


def print_people(people: list[Person]) -> None:
    for person in people:
        print(person)

def multi_parser():
    path = get_path()
    ext = get_extension(path)

    match ext:
        case ".xml":
            try:
                elements = ElementTree.parse(path)
                root_element = elements.getroot()
                people: list[Person] = []

                for person in root_element.findall('Person'):
                    person_id = person.get('id')
                    name = person.findtext('Name')
                    age_text = person.findtext('Age')
                    city = person.findtext('City')
                    
                    people.append(
                        to_person(
                            person_id=person_id,
                            name=name,
                            age=age_text,
                            city=city,
                        )
                    )

                print_people(people)
                    
            except ElementTree.ParseError as e:
                print('Failed to parse XML file: ', e)
            return []
        
        
        case ".json":
            people: list[Person] = []
            try:
                with open(path, mode="r") as json_file:
                    data = json.load(json_file)
            except OSError as e:
                print("Failed to read json file: ", e)
                return []
            except json.JSONDecodeError as e:
                print("Failed to decode json file: ", e)
                return []

            for person in data:
                people.append(
                    to_person(
                        person_id=person["Id"],
                        name=person["Name"],
                        age=person["Age"],
                        city=person["City"],
                    )
                )
                
            print_people(people)

        case ".csv":
            people: list[Person]= []

            try:
                with open(path, mode='r') as csv_file:
                    reader = csv.DictReader(csv_file, delimiter=',')
                    
                    for row in reader:
                        people.append(
                            to_person(
                                person_id=row["id"],
                                name=row["name"],
                                age=row["age"],
                                city=row["city"],
                            )
                        )
            except OSError as e:
                print('Failed to read file: ', e)

            print_people(people)
            
        case _:
            print("Extension not in list or not provided")


def main():
    multi_parser()


if __name__ == "__main__":
    main()
