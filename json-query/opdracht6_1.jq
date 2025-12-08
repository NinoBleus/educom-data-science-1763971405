map({ country: .country, 
        population_1970: .population_1970, 
        area_km2: .area_km2, 
        population_density: .population_density, 
        population_density_1970: .population_1970/.area_km2})
| (["country","population_1970", "area_km2", "population_density", "population_density_1970"] | @csv),         #excel rows header
  (.[] | [.country, .population_1970, .area_km2, .population_density, .population_density_1970] | @csv)        #excel rows data
