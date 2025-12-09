group_by(.continent)
| map({
    continent: .[0].continent,
    growth_percentage_compared_to_1970:
      (map((.population_2022 - .population_1970) / .population_1970) * 100| add)
  })
| (["continent","growth_percentage_compared_to_1970"] | @csv),      #excel rows header
  (.[] | [.continent, .growth_percentage_compared_to_1970] | @csv)  #excel rows data
