import json
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "jsonqueryplayground"
)

mycursor = mydb.cursor()

sql = "INSERT INTO jsondata (`rank`, " \
                            "cca3, " \
                            "country, " \
                            "capital, " \
                            "continent, " \
                            "population_2022, " \
                            "population_2020, " \
                            "population_2015, " \
                            "population_2010, " \
                            "population_2000, " \
                            "population_1990, " \
                            "population_1980, " \
                            "population_1970, " \
                            "area_km2, " \
                            "population_density, " \
                            "population_growth_rate, " \
                            "percentage_world_population) " \
                            "VALUES (" \
                            "%s," \
                            "%s," \
                            "%s," \
                            "%s," \
                            "%s," \
                            "%s," \
                            "%s," \
                            "%s," \
                            "%s," \
                            "%s," \
                            "%s," \
                            "%s," \
                            "%s," \
                            "%s," \
                            "%s," \
                            "%s," \
                            "%s)"



with open("world-population.json", "r", encoding="utf-8") as f:
    data = json.load(f)


for item in data:
    params = (
        item["rank"],
        item["cca3"],
        item["country"],
        item["capital"],
        item["continent"],
        item["population_2022"],
        item["population_2020"],
        item["population_2015"],
        item["population_2010"],
        item["population_2000"],
        item["population_1990"],
        item["population_1980"],
        item["population_1970"],
        item["area_km2"],
        item["population_density"],
        item["population_growth_rate"],
        item["percentage_world_population"]
    )
    mycursor.execute(sql, params)
    
    
mydb.commit()
print(mycursor.rowcount, "record inserted.")
   
    