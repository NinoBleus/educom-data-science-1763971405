# Opdracht 1
---
## V1
```bash
jq 'map({country: .country, population_1970: .population_1970, area_km2: .area_km2, population_density: .population_density, population_density_1970: .population_1970/.area_km2})' < world-population.json > opdracht1.json
```
## Output
```json
{
  "country": "Afghanistan",
  "population_1970": 10752971,
  "area_km2": 652230,
  "population_density": 63.0587,
  "population_density_1970": 16.48647103015807
}
{
  "country": "Albania",
  "population_1970": 2324731,
  "area_km2": 28748,
  "population_density": 98.8702,
  "population_density_1970": 80.86583414498399
}
{
  "country": "Algeria",
  "population_1970": 13795915,
  "area_km2": 2381741,
  "population_density": 18.8531,
  "population_density_1970": 5.792365752615419
}
{...}
```
# Opdracht 2
---
## V1
```bash
jq 'group_by(.continent) | map({continent: .[0].continent, total_growth: (map(.population_2022 - .population_1970) | add)})' < world-population.json > opdracht2.json
```
## Output
```json
[
  {
    "continent": "Africa",
    "total_growth": 1061286584
  },
  {
    "continent": "Asia",
    "total_growth": 2576476984
  },
  {
    "continent": "Europe",
    "total_growth": 87223547
  },
  {
    "continent": "North America",
    "total_growth": 284861530
  },
  {
    "continent": "Oceania",
    "total_growth": 25558284
  },
  {
    "continent": "South America",
    "total_growth": 243869452
  }
]
```
# Opdracht 3
---
## V1
```bash
jq 'group_by(.continent) | map({continent: .[0].continent, population_2022: (map(.population_2022) | add), population_2020: (map(.population_2020) | add), population_2015: (map(.population_2015) | add), population_2010: (map(.population_2010) | add), population_2000: (map(.population_2000) | add), population_1990: (map(.population_1990) | add), population_1980: (map(.population_1980) | add), population_1970: (map(.population_1970) | add)})' < world-population.json 
```
## V2
```bash
jq 'group_by(.continent) | map(. as $g | { continent: $g[0].continent } + ( reduce ["population_2022","population_2020","population_2015", "population_2010","population_2000","population_1990", "population_1980","population_1970"][] as $k ({}; . + { ($k): ($g | map(.[$k]) | add) } ) ) )' < world-population.json > opdracht3.json
```
## output
```json
[
  {
    "continent": "Africa",
    "population_2022": 1426730932,
    "population_2020": 1360671810,
    "population_2015": 1201102442,
    "population_2010": 1055228072,
    "population_2000": 818946032,
    "population_1990": 638150629,
    "population_1980": 481536377,
    "population_1970": 365444348
  },
  {
    "continent": "Asia",
    "population_2022": 4721383274,
    "population_2020": 4663086535,
    "population_2015": 4458250182,
    "population_2010": 4220041327,
    "population_2000": 3735089604,
    "population_1990": 3210563577,
    "population_1980": 2635334228,
    "population_1970": 2144906290
  },
  {
    "continent": "Europe",
    "population_2022": 743147538,
    "population_2020": 745792196,
    "population_2015": 741535608,
    "population_2010": 735613934,
    "population_2000": 726093423,
    "population_1990": 720320797,
    "population_1980": 692527159,
    "population_1970": 655923991
  },
  {
    "continent": "North America",
    "population_2022": 600296136,
    "population_2020": 594236593,
    "population_2015": 570383850,
    "population_2010": 542720651,
    "population_2000": 486069584,
    "population_1990": 421266425,
    "population_1980": 368293361,
    "population_1970": 315434606
  },
  {
    "continent": "Oceania",
    "population_2022": 45038554,
    "population_2020": 43933426,
    "population_2015": 40403283,
    "population_2010": 37102764,
    "population_2000": 31222778,
    "population_1990": 26743822,
    "population_1980": 22920240,
    "population_1970": 19480270
  },
  {
    "continent": "South America",
    "population_2022": 436816608,
    "population_2020": 431530043,
    "population_2015": 413134396,
    "population_2010": 393078250,
    "population_2000": 349634282,
    "population_1990": 297146415,
    "population_1980": 241789006,
    "population_1970": 192947156
  }
]
```
# Opdracht 4
---
## V1
```bash
$ jq 'group_by(.continent) | map({continent: .[0].continent, percentage_world_population: (map(.percentage_world_population) | add)})' < world-population.json > opdracht4.json
```
## Output
```json
[
  {
    "continent": "Africa",
    "percentage_world_population": 17.869999999999997
  },
  {
    "continent": "Asia",
    "percentage_world_population": 59.19
  },
  {
    "continent": "Europe",
    "percentage_world_population": 9.33
  },
  {
    "continent": "North America",
    "percentage_world_population": 7.51
  },
  {
    "continent": "Oceania",
    "percentage_world_population": 0.55
  },
  {
    "continent": "South America",
    "percentage_world_population": 5.4799999999999995
  }
]
```
# Opdracht 5
## V1
```bash
jq 'group_by(.continent) | map({continent: .[0].continent, growth_percentage_compared_to_1970: (map((.population_2022 - .population_1970) / .population_1970) | add)})' < world-population.json > opdracht5.json
```
## Output
```json
[
  {
    "continent": "Africa",
    "growth_percentage_compared_to_1970": 170.99350036578141
  },
  {
    "continent": "Asia",
    "growth_percentage_compared_to_1970": 149.97474044362724
  },
  {
    "continent": "Europe",
    "growth_percentage_compared_to_1970": 15.113042662478312
  },
  {
    "continent": "North America",
    "growth_percentage_compared_to_1970": 56.667844400975056
  },
  {
    "continent": "Oceania",
    "growth_percentage_compared_to_1970": 26.08601167964653
  },
  {
    "continent": "South America",
    "growth_percentage_compared_to_1970": 20.235005160146557
  }
]
```
# Opdracht 6
## V1
See .jq files
# Opdracht 7
## V1
```bash
jq '
  map({
    rank: .rank,
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
    percentage_world_population: .percentage_world_population
  })
' world-population.json
```
## Output
```json
[
  {...},
  {
    "rank": 79,
    "cca3": "TUN",
    "country": "Tunisia",
    "capital": "Tunis",
    "continent": "Africa",
    "population": [
      {
        "year": "2022",
        "amount": 12356117
      },
      {
        "year": "2020",
        "amount": 12161723
      },
      {
        "year": "2015",
        "amount": 11557779
      },
      {
        "year": "2010",
        "amount": 10895063
      },
      {
        "year": "2000",
        "amount": 9893316
      },
      {
        "year": "1990",
        "amount": 8440023
      },
      {
        "year": "1980",
        "amount": 6578156
      },
      {
        "year": "1970",
        "amount": 5047404
      }
    ],
    "area_km2": 163610,
    "population_density": 75.5218,
    "population_growth_rate": 1.0076,
    "percentage_world_population": 0.15
  },
  {
    "rank": 18,
    "cca3": "TUR",
    "country": "Turkey",
    "capital": "Ankara",
    "continent": "Asia",
    "population": [
      {
        "year": "2022",
        "amount": 85341241
      },
      {
        "year": "2020",
        "amount": 84135428
      },
      {
        "year": "2015",
        "amount": 79646178
      },
      {
        "year": "2010",
        "amount": 73195345
      },
      {
        "year": "2000",
        "amount": 64113547
      },
      {
        "year": "1990",
        "amount": 54324142
      },
      {
        "year": "1980",
        "amount": 44089069
      },
      {
        "year": "1970",
        "amount": 35540990
      }
    ],
    "area_km2": 783562,
    "population_density": 108.9145,
    "population_growth_rate": 1.0067,
    "percentage_world_population": 1.07
  },
  {...}
]
```