map({   rank: .rank,
        cca3: .cca3,
        country: .country,
        capital: .capital,
        continent: .continent,
        population: 
           (to_entries 
            | map(
                select(.key | test("^population_[0-9]{4}$"))
                | { year: (.key | ltrimstr("population_")), amount: .value }
                )
            ),
        area_km2: .area_km2,
        population_density: .population_density,
        population_growth_rate: .population_growth_rate,
        percentage_world_population: .percentage_world_population})