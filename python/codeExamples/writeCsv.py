import csv
import sys
from dataclasses import dataclass

@dataclass
class Person:
    id: int
    name: str
    age: int
    city: str

def write_csv(file_path: str, persons: list[object]) -> bool:

    if len(persons) < 1:
        print('List empty: nothing to write')
        return False

    try:
        with open(file_path, mode='w') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            first_attributes = vars(persons[0])
            field_names = list(first_attributes.keys())
            writer.writerow(field_names)

            for person in persons:
                person_attributes = vars(person)
                if person_attributes.keys() != first_attributes.keys():
                    print('Objects do not share the same attributes')
                    return False
                row = [person_attributes[name] for name in field_names]
                writer.writerow(row)
            return True

    except OSError as e:
        print('Failed to write to CSV file: ', e)
    
    return False

def main():
    args = sys.argv[1:]
    if len(args) < 5 or (len(args) - 1) % 4 != 0:
        print('Usage: python writeCsv.py <path> <id> <name> <age> <city> [<id> <name> <age> <city> ...]')
        return

    path = args[0]
    people_args = args[1:]
    persons: list[Person] = []
    for i in range(0, len(people_args), 4):
        persons.append(
            Person(
                id=int(people_args[i]),
                name=people_args[i + 1],
                age=int(people_args[i + 2]),
                city=people_args[i + 3],
            )
        )

    succes = write_csv(path, persons)
    if succes:
        print("Succesfully wrote text in file")
    else:
        print("Couldn't write in file")


if __name__ == "__main__":
    main()
