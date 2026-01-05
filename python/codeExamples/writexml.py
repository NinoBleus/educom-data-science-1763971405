import xml.etree.ElementTree as ElementTree
import sys
from typing import List
from dataclasses import dataclass


@dataclass
class Person:
    id: int
    name: str
    age: int
    city: str


def write_people_to_xml(file_path: str, persons: List[Person]):
    xml_string = get_persons_xml_string(persons)

    try:
        with open(file_path, mode='w') as xml_file:
            xml_file.write(xml_string)

    except OSError as e:
        print('Failed to write to XML file: ', e)


def get_persons_xml_string(persons: List[Person]) -> str:
    root_element = ElementTree.Element('ArrayOfPerson')
    for person in persons:
        add_person_element(person, root_element)

    ElementTree.indent(root_element, space="  ", level=0)
    xml_string = ElementTree.tostring(root_element, encoding="unicode", xml_declaration=True)
    return xml_string


def add_person_element(person: Person, root_element):
    person_element = ElementTree.SubElement(root_element, 'Person')
    person_element.set('id', str(person.id))
    name_element = ElementTree.SubElement(person_element, 'Name')
    name_element.text = person.name
    age_element = ElementTree.SubElement(person_element, 'Age')
    age_element.text = str(person.age)
    city_element = ElementTree.SubElement(person_element, 'City')
    city_element.text = person.city
    
    
    
def get_path() -> str:
    try:
        return sys.argv[1]
    except IndexError:
        return ''
    

def get_content() -> list[str]:
    try:
        return sys.argv[2:]
    except IndexError:
        return []


def string_to_object(input_string: list[str]) -> list[Person]:
    persons: list[Person] = []
    for i in range(0, len(input_string), 4):
        persons.append(
            Person(
                id=int(input_string[i]),
                name=input_string[i + 1],
                age=int(input_string[i + 2]),
                city=input_string[i + 3],
            )
        )
    return persons
    
    
def main():
    path = get_path()
    content = get_content()
    persons = string_to_object(content)
    write_people_to_xml(path, persons)
    if path:
        print('Succesfully wrote text to xml')
    else:
        print("Couldn't write text to file")


if __name__ == "__main__":
    main()
