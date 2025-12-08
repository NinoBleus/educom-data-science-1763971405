group_by(.continent) 
| map({ continent: .[0].continent, 
        percentage_world_population: (map(.percentage_world_population) | add)})
| (["continent",
    "percentage_world_population"] 
| @csv),         #excel rows header
  (.[] 
| [ .continent, 
    .percentage_world_population] 
| @csv)        #excel rows data
