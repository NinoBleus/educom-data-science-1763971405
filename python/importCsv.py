import csv
import sys
from dataclasses import dataclass

@dataclass
class Person:
    id: str
    name: str
    age: int
    city: str

def read_csv() -> list[Person]:
    path = 'data/'+get_path()
    rows = []
    people: list[Person]= []

    try:
        with open(path, mode='r') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=',')
            
            for row in reader:
                  people.append(
                    Person(
                        id=row["id"],
                        name=row["name"],
                        age=int(row["age"]),
                        city=row["city"],
                    )
                )
    except OSError as e:
        print('Failed to read file: ', e)

    return people


def get_path() -> str:
    try:
        return sys.argv[1]
    except IndexError:
        return ''
    

def main():
    csv_content = read_csv()
    for person in csv_content:
        print(person)
    

if __name__ == "__main__":
    main()
