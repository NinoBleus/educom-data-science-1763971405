group_by(.continent) | map({continent: .[0].continent, total_growth: (map(.population_2022 - .population_1970) | add)})
| (["continent","total_growth"] | @csv),        #excel rows header
  (.[] | [.continent, .total_growth] | @csv)    #excel rows data
