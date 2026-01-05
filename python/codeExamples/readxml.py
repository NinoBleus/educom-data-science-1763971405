import xml.etree.ElementTree as ElementTree
import sys
from dataclasses import dataclass


@dataclass
class Person:
    id: int
    name: str
    age: int
    city: str

def print_people_from_xml(file_path: str):
    try:
        elements = ElementTree.parse(file_path)
        root_element = elements.getroot()

        for person in root_element:
            print('id:', person.get('id'))
            for element in person:
                print(element.tag + ':', element.text)
                
    except ElementTree.ParseError as e:
        print('Failed to parse XML file: ', e)


def people_from_xml(file_path: str) -> list[Person]:
    try:
        elements = ElementTree.parse(file_path)
        root_element = elements.getroot()
        people: list[Person] = []

        for person in root_element.findall('Person'):
            person_id = person.get('id')
            name = person.findtext('Name')
            age_text = person.findtext('Age')
            city = person.findtext('City')

            people.append(
                Person(
                    id=int(person_id),
                    name=name,
                    age=int(age_text),
                    city=city,
                )
            )

        return people
    except ElementTree.ParseError as e:
        print('Failed to parse XML file: ', e)

    return []


def get_path() -> str:
    try:
        return sys.argv[1]
    except IndexError:
        print("Path doesn't exist or is wrong")


def main():
    path = get_path()
    people = people_from_xml(path)
    for person in people:
        print(person)


if __name__ == "__main__":
    main()
