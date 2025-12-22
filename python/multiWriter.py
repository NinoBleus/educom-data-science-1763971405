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
    return Path(file_path).suffix


def get_path() -> str:
    try:
        return sys.argv[1]
    except IndexError:
        print("Path doesn't exist or is wrong.")
        return ''


def get_content() -> list[str]:
    try:
        return sys.argv[2:]
    except IndexError:
        return []


def to_person(person_id, name, age, city) -> Person:
    return Person(
        id=int(person_id),
        name=name,
        age=int(age),
        city=city,
    )


def string_to_object(input_string: list[str]) -> list[Person]:
    people: list[Person] = []
    for i in range(0, len(input_string), 4):
        people.append(
            to_person(
                person_id=input_string[i],
                name=input_string[i + 1],
                age=input_string[i + 2],
                city=input_string[i + 3],
            )
        )
    return people


def people_to_json(people: list[Person]) -> list[dict]:
    return [
        {"Id": person.id, "Name": person.name, "Age": person.age, "City": person.city}
        for person in people
    ]


def write_json(file_path: str, people: list[Person]) -> bool:
    try:
        with open(file_path, mode='w') as json_file:
            json.dump(people_to_json(people), json_file, indent=2)
        return True
    except OSError as e:
        print('Failed to write to json file: ', e)
    return False


def write_csv(file_path: str, people: list[Person]) -> bool:
    try:
        with open(file_path, mode='w', newline='') as csv_file:
            fieldnames = ['id', 'name', 'age', 'city']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for person in people:
                writer.writerow(
                    {
                        "id": person.id,
                        "name": person.name,
                        "age": person.age,
                        "city": person.city,
                    }
                )
        return True
    except OSError as e:
        print('Failed to write to csv file: ', e)
    return False


def add_person_element(person: Person, root_element):
    person_element = ElementTree.SubElement(root_element, 'Person')
    person_element.set('id', str(person.id))
    name_element = ElementTree.SubElement(person_element, 'Name')
    name_element.text = person.name
    age_element = ElementTree.SubElement(person_element, 'Age')
    age_element.text = str(person.age)
    city_element = ElementTree.SubElement(person_element, 'City')
    city_element.text = person.city


def write_xml(file_path: str, people: list[Person]) -> bool:
    root_element = ElementTree.Element('ArrayOfPerson')
    for person in people:
        add_person_element(person, root_element)
    ElementTree.indent(root_element, space="  ", level=0)
    xml_string = ElementTree.tostring(root_element, encoding="unicode", xml_declaration=True)
    try:
        with open(file_path, mode='w') as xml_file:
            xml_file.write(xml_string)
        return True
    except OSError as e:
        print('Failed to write to XML file: ', e)
    return False


def multi_writer():
    path = get_path()
    if not path:
        print("Extension not in list or not provided")
        return

    ext = get_extension(path)
    people = string_to_object(get_content())

    match ext:
        case ".xml":
            success = write_xml(path, people)
        case ".json":
            success = write_json(path, people)
        case ".csv":
            success = write_csv(path, people)
        case _:
            print("Extension not in list or not provided")
            return

    if success:
        print("Succesfully wrote file")
    else:
        print("Couldn't write text to file")


def main():
    multi_writer()


if __name__ == "__main__":
    main()
