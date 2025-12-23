import mysql.connector
import os, sys
from dotenv import load_dotenv
from dataclasses import dataclass
from json import JSONDecodeError, load

load_dotenv()

@dataclass
class Person:
    id: int
    name: str
    age: int
    city: str

def get_connection():  
    db_connection = mysql.connector.connect(
        host = os.getenv("DATABASE_host"),
        user = os.getenv("DATABASE_user"),
        passwd = os.getenv("DATABASE_passwd"),
        database = os.getenv("DATABASE_database")
    )
    return db_connection


def get_persons_simple(db_connection) -> list[Person]:
    db_cursor = db_connection.cursor()
    query = "SELECT * FROM person"
    db_cursor.execute(query)

    results = db_cursor.fetchall()
    persons = []

    for (id, name, age, city) in results:
        new_person = Person(id, name, age, city)
        persons.append(new_person)

    db_cursor.close()

    return persons


def get_persons_advanced(db_connection) -> list[Person]:
    db_cursor = db_connection.cursor(buffered=True, dictionary=True)
    query = "SELECT * FROM person"
    db_cursor.execute(query)
    persons = []

    for row in db_cursor:
        new_person = Person(**row)
        persons.append(new_person)

    db_cursor.close()
    
    return persons

def add_or_update_person_to_db(person: object, db_connection) -> tuple[object, bool]:

    db_cursor = db_connection.cursor()
    table = type(person).__name__.lower()
    data = dict(person.__dict__)
    person_id = data.get("id")
    columns = [key for key in data.keys() if key != "id"]

    if person_id:
        set_clause = ", ".join(f"{column}=%s" for column in columns)
        query = f"UPDATE {table} SET {set_clause} WHERE id=%s"
        values = [data[column] for column in columns] + [person_id]
    else:
        placeholders = ", ".join(["%s"] * len(columns))
        column_clause = ", ".join(columns)
        query = f"INSERT INTO {table} ({column_clause}) VALUES ({placeholders})"
        values = [data[column] for column in columns]

    db_cursor.execute(query, values)
    changed = db_cursor.rowcount > 0

    if not person_id:
        person.id = db_cursor.lastrowid
        
    db_connection.commit()
    db_cursor.close()

    return person, changed

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

def json_to_object(json) -> list[Person]:
    people: list[Person] = []
    for person in json:
        people.append(
            Person(
                id=int(person["Id"]),
                name=person["Name"],
                age=int(person["Age"]),
                city=person["City"],
            )
        )
    
    return people


def read_json_add_update_database(path, db_connection) -> bool:
    json = read_json(path)
    jsonObject = json_to_object(json)
    if not jsonObject:
        print("No people found to process.")
        return False
    try:
        any_changed = False
        for person in jsonObject:
            result, changed = add_or_update_person_to_db(person, db_connection)
            if changed:
                any_changed = True
                print(result)
            else:
                print(f"No changes for id {result.id}.")
        if not any_changed:
            print("No changes were applied to the database.")
        return True
    except Exception as e:
        print("Failed to add/update people:", e)
        return False
    

def get_path() -> str:
    try:
        return sys.argv[1]
    except IndexError:
        print("Path doesn't exist or is wrong")
        

def main():
    db_con = get_connection()
    path = get_path()
    result = read_json_add_update_database(path, db_con)
    if result:
        print("Successfully done operation.")
    else:
        print("Failed to do operation.")
        
    
    
    
    
if __name__ == "__main__":
    main()
