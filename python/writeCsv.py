import csv
import sys
from dataclasses import dataclass

@dataclass
class Person:
    id: str
    name: str
    age: int
    city: str

def write_csv(file_path: str, persons: list[Person]) -> bool:

    if len(persons) < 1:
        print('List empty: nothing to write')
        return False

    try:
        with open(file_path, mode='w') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            field_names = ['id', 'name', 'age', 'city']
            writer.writerow(field_names)

            for person in persons:
                row = [person.id, person.name, person.age, person.city]
                writer.writerow(row)
            return True

    except OSError as e:
        print('Failed to write to CSV file: ', e)
    
    return False



def main(path, Person):
    succes = write_csv(path, Person)
    if succes:
        print("Succesfully wrote text in file")
    else:
        print("Couldn't write in file")


if __name__ == "__main__":
    main()