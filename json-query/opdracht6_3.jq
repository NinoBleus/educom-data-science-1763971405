group_by(.continent) 
| map(. as $g | { continent: $g[0].continent } + 
                ( reduce [  "population_2022",
                            "population_2020",
                            "population_2015",
                            "population_2010",
                            "population_2000",
                            "population_1990", 
                            "population_1980",
                            "population_1970"]
                            [] as $k ({}; . + { ($k): ($g | map(.[$k]) | add) } ) ) )
| (["continent",
    "population_2022",
    "population_2020",
    "population_2015",
    "population_2010",
    "population_2000",
    "population_1990", 
    "population_1980",
    "population_1970"] 
| @csv),         #excel rows header
  (.[] 
| [ .continent, 
    .population_2022, 
    .population_2020, 
    .population_2015, 
    .population_2010,
    .population_2000,
    .population_1990,
    .population_1980,
    .population_1970] 
| @csv)        #excel rows data
