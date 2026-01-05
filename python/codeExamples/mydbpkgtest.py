from mydbpkg import get_connection, create_or_update, read_one, read_all, delete

# read all
readAll = read_all("person")
print(readAll, end="\n\n")

# create
new_id, changed = create_or_update("person", {"name": "Ada", "age": 30, "city": "AMS"})
row = read_one("person", new_id)
print(row, end="\n\n")

# update
existing_id = create_or_update("person", {"id": new_id, "name": "Adam and Eve", "age": 31, "city": "Amsterdam"})
print(existing_id, end= "\n\n")

# delete
delete_id = delete("person", new_id)
print(delete_id, end="\n\n")
