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
{
  "country": "American Samoa",
  "population_1970": 27075,
  "area_km2": 199,
  "population_density": 222.4774,
  "population_density_1970": 136.05527638190955
}
{
  "country": "Andorra",
  "population_1970": 19860,
  "area_km2": 468,
  "population_density": 170.5641,
  "population_density_1970": 42.43589743589744
}
{
  "country": "Angola",
  "population_1970": 6029700,
  "area_km2": 1246700,
  "population_density": 28.5466,
  "population_density_1970": 4.836528435068581
}
{
  "country": "Anguilla",
  "population_1970": 6283,
  "area_km2": 91,
  "population_density": 174.2527,
  "population_density_1970": 69.04395604395604
}
{
  "country": "Antigua and Barbuda",
  "population_1970": 64516,
  "area_km2": 442,
  "population_density": 212.1335,
  "population_density_1970": 145.96380090497738
}
{
  "country": "Argentina",
  "population_1970": 23842803,
  "area_km2": 2780400,
  "population_density": 16.3683,
  "population_density_1970": 8.575313983599482
}
{
  "country": "Armenia",
  "population_1970": 2534377,
  "area_km2": 29743,
  "population_density": 93.4831,
  "population_density_1970": 85.20919207880846
}
{
  "country": "Aruba",
  "population_1970": 59106,
  "area_km2": 180,
  "population_density": 591.3611,
  "population_density_1970": 328.3666666666667
}
{
  "country": "Australia",
  "population_1970": 12595034,
  "area_km2": 7692024,
  "population_density": 3.4032,
  "population_density_1970": 1.6374148078581139
}
{
  "country": "Austria",
  "population_1970": 7465301,
  "area_km2": 83871,
  "population_density": 106.5877,
  "population_density_1970": 89.00932384256775
}
{
  "country": "Azerbaijan",
  "population_1970": 5425317,
  "area_km2": 86600,
  "population_density": 119.6082,
  "population_density_1970": 62.64800230946882
}
{
  "country": "Bahamas",
  "population_1970": 179129,
  "area_km2": 13943,
  "population_density": 29.4043,
  "population_density_1970": 12.84723517177078
}
{
  "country": "Bahrain",
  "population_1970": 222555,
  "area_km2": 765,
  "population_density": 1924.4876,
  "population_density_1970": 290.921568627451
}
{
  "country": "Bangladesh",
  "population_1970": 67541860,
  "area_km2": 147570,
  "population_density": 1160.035,
  "population_density_1970": 457.69370468252356
}
{
  "country": "Barbados",
  "population_1970": 241397,
  "area_km2": 430,
  "population_density": 654.9651,
  "population_density_1970": 561.3883720930232
}
{
  "country": "Belarus",
  "population_1970": 9170786,
  "area_km2": 207600,
  "population_density": 45.9295,
  "population_density_1970": 44.17526974951831
}
{
  "country": "Belgium",
  "population_1970": 9629376,
  "area_km2": 30528,
  "population_density": 381.8111,
  "population_density_1970": 315.42767295597486
}
{
  "country": "Belize",
  "population_1970": 120905,
  "area_km2": 22966,
  "population_density": 17.6466,
  "population_density_1970": 5.264521466515719
}
{
  "country": "Benin",
  "population_1970": 3023443,
  "area_km2": 112622,
  "population_density": 118.5635,
  "population_density_1970": 26.845935962778142
}
{
  "country": "Bermuda",
  "population_1970": 52019,
  "area_km2": 54,
  "population_density": 1188.5926,
  "population_density_1970": 963.3148148148148
}
{
  "country": "Bhutan",
  "population_1970": 298894,
  "area_km2": 38394,
  "population_density": 20.3796,
  "population_density_1970": 7.78491430952753
}
{
  "country": "Bolivia",
  "population_1970": 4585693,
  "area_km2": 1098581,
  "population_density": 11.1272,
  "population_density_1970": 4.174196531707721
}
{
  "country": "Bosnia and Herzegovina",
  "population_1970": 3815561,
  "area_km2": 51209,
  "population_density": 63.1437,
  "population_density_1970": 74.50957839442286
}
{
  "country": "Botswana",
  "population_1970": 592244,
  "area_km2": 582000,
  "population_density": 4.5194,
  "population_density_1970": 1.0176013745704466
}
{
  "country": "Brazil",
  "population_1970": 96369875,
  "area_km2": 8515767,
  "population_density": 25.2841,
  "population_density_1970": 11.316640650219762
}
{
  "country": "British Virgin Islands",
  "population_1970": 9581,
  "area_km2": 151,
  "population_density": 207.3179,
  "population_density_1970": 63.450331125827816
}
{
  "country": "Brunei",
  "population_1970": 133343,
  "area_km2": 5765,
  "population_density": 77.8841,
  "population_density_1970": 23.129748482220293
}
{
  "country": "Bulgaria",
  "population_1970": 8582950,
  "area_km2": 110879,
  "population_density": 61.1654,
  "population_density_1970": 77.40825584646326
}
{
  "country": "Burkina Faso",
  "population_1970": 5611666,
  "area_km2": 272967,
  "population_density": 83.0641,
  "population_density_1970": 20.55803815113182
}
{
  "country": "Burundi",
  "population_1970": 3497834,
  "area_km2": 27834,
  "population_density": 463.0874,
  "population_density_1970": 125.66767263059567
}
{
  "country": "Cambodia",
  "population_1970": 6708525,
  "area_km2": 181035,
  "population_density": 92.6221,
  "population_density_1970": 37.05650840997597
}
{
  "country": "Cameroon",
  "population_1970": 6452787,
  "area_km2": 475442,
  "population_density": 58.7128,
  "population_density_1970": 13.57218546110777
}
{
  "country": "Canada",
  "population_1970": 21434577,
  "area_km2": 9984670,
  "population_density": 3.8513,
  "population_density_1970": 2.146748665704525
}
{
  "country": "Cape Verde",
  "population_1970": 287262,
  "area_km2": 4033,
  "population_density": 147.0739,
  "population_density_1970": 71.22787007190676
}
{
  "country": "Cayman Islands",
  "population_1970": 10533,
  "area_km2": 264,
  "population_density": 260.25,
  "population_density_1970": 39.89772727272727
}
{
  "country": "Central African Republic",
  "population_1970": 2067356,
  "area_km2": 622984,
  "population_density": 8.9555,
  "population_density_1970": 3.3184736686656477
}
{
  "country": "Chad",
  "population_1970": 3667394,
  "area_km2": 1284000,
  "population_density": 13.8032,
  "population_density_1970": 2.856225856697819
}
{
  "country": "Chile",
  "population_1970": 9820481,
  "area_km2": 756102,
  "population_density": 25.9274,
  "population_density_1970": 12.988301842873051
}
{
  "country": "China",
  "population_1970": 822534450,
  "area_km2": 9706961,
  "population_density": 146.8933,
  "population_density_1970": 84.73655658037568
}
{
  "country": "Colombia",
  "population_1970": 20905254,
  "area_km2": 1141748,
  "population_density": 45.4339,
  "population_density_1970": 18.30986697590011
}
{
  "country": "Comoros",
  "population_1970": 242351,
  "area_km2": 1862,
  "population_density": 449.3953,
  "population_density_1970": 130.156283566058
}
{
  "country": "Cook Islands",
  "population_1970": 20470,
  "area_km2": 236,
  "population_density": 72.0805,
  "population_density_1970": 86.73728813559322
}
{
  "country": "Costa Rica",
  "population_1970": 1855697,
  "area_km2": 51100,
  "population_density": 101.3861,
  "population_density_1970": 36.315009784735814
}
{
  "country": "Croatia",
  "population_1970": 4492638,
  "area_km2": 56594,
  "population_density": 71.2153,
  "population_density_1970": 79.38364490935435
}
{
  "country": "Cuba",
  "population_1970": 8869636,
  "area_km2": 109884,
  "population_density": 102.0366,
  "population_density_1970": 80.7181755305595
}
{
  "country": "Curacao",
  "population_1970": 150385,
  "area_km2": 444,
  "population_density": 430.5473,
  "population_density_1970": 338.7049549549549
}
{
  "country": "Cyprus",
  "population_1970": 640804,
  "area_km2": 9251,
  "population_density": 135.2814,
  "population_density_1970": 69.26861960869095
}
{
  "country": "Czech Republic",
  "population_1970": 9795744,
  "area_km2": 78865,
  "population_density": 133.0627,
  "population_density_1970": 124.20901540607368
}
{
  "country": "Denmark",
  "population_1970": 4922963,
  "area_km2": 43094,
  "population_density": 136.4984,
  "population_density_1970": 114.2377825219288
}
{
  "country": "Djibouti",
  "population_1970": 144379,
  "area_km2": 23200,
  "population_density": 48.3125,
  "population_density_1970": 6.223232758620689
}
{
  "country": "Dominica",
  "population_1970": 68895,
  "area_km2": 751,
  "population_density": 96.8535,
  "population_density_1970": 91.73768308921439
}
{
  "country": "Dominican Republic",
  "population_1970": 4475871,
  "area_km2": 48671,
  "population_density": 230.7087,
  "population_density_1970": 91.96176367857656
}
{
  "country": "DR Congo",
  "population_1970": 20151733,
  "area_km2": 2344858,
  "population_density": 42.2244,
  "population_density_1970": 8.594009957106145
}
{
  "country": "Ecuador",
  "population_1970": 6172215,
  "area_km2": 276841,
  "population_density": 65.0229,
  "population_density_1970": 22.295162205020212
}
{
  "country": "Egypt",
  "population_1970": 34781986,
  "area_km2": 1002450,
  "population_density": 110.7188,
  "population_density_1970": 34.69697840291286
}
{
  "country": "El Salvador",
  "population_1970": 3619090,
  "area_km2": 21041,
  "population_density": 301.145,
  "population_density_1970": 172.0018059978138
}
{
  "country": "Equatorial Guinea",
  "population_1970": 316955,
  "area_km2": 28051,
  "population_density": 59.7094,
  "population_density_1970": 11.299240668781861
}
{
  "country": "Eritrea",
  "population_1970": 1272748,
  "area_km2": 117600,
  "population_density": 31.3268,
  "population_density_1970": 10.822687074829933
}
{
  "country": "Estonia",
  "population_1970": 1361999,
  "area_km2": 45227,
  "population_density": 29.3201,
  "population_density_1970": 30.114732350144823
}
{
  "country": "Eswatini",
  "population_1970": 442865,
  "area_km2": 17364,
  "population_density": 69.2047,
  "population_density_1970": 25.504780004607234
}
{
  "country": "Ethiopia",
  "population_1970": 28308246,
  "area_km2": 1104300,
  "population_density": 111.7268,
  "population_density_1970": 25.63456126052703
}
{
  "country": "Falkland Islands",
  "population_1970": 2274,
  "area_km2": 12173,
  "population_density": 0.3105,
  "population_density_1970": 0.18680686765793147
}
{
  "country": "Faroe Islands",
  "population_1970": 38416,
  "area_km2": 1393,
  "population_density": 38.112,
  "population_density_1970": 27.57788944723618
}
{
  "country": "Fiji",
  "population_1970": 527634,
  "area_km2": 18272,
  "population_density": 50.8847,
  "population_density_1970": 28.876641856392293
}
{
  "country": "Finland",
  "population_1970": 4606621,
  "area_km2": 338424,
  "population_density": 16.3722,
  "population_density_1970": 13.611980828782828
}
{
  "country": "France",
  "population_1970": 50523586,
  "area_km2": 551695,
  "population_density": 117.1419,
  "population_density_1970": 91.57883613228324
}
{
  "country": "French Guiana",
  "population_1970": 46484,
  "area_km2": 83534,
  "population_density": 3.6459,
  "population_density_1970": 0.55646802499581
}
{
  "country": "French Polynesia",
  "population_1970": 117891,
  "area_km2": 4167,
  "population_density": 73.5011,
  "population_density_1970": 28.29157667386609
}
{
  "country": "Gabon",
  "population_1970": 597192,
  "area_km2": 267668,
  "population_density": 8.9252,
  "population_density_1970": 2.231092248606483
}
{
  "country": "Gambia",
  "population_1970": 528731,
  "area_km2": 10689,
  "population_density": 253.1567,
  "population_density_1970": 49.464963981663395
}
{
  "country": "Georgia",
  "population_1970": 4800426,
  "area_km2": 69700,
  "population_density": 53.7214,
  "population_density_1970": 68.87268292682927
}
{
  "country": "Germany",
  "population_1970": 78294583,
  "area_km2": 357114,
  "population_density": 233.4544,
  "population_density_1970": 219.2425471978136
}
{
  "country": "Ghana",
  "population_1970": 8861895,
  "area_km2": 238533,
  "population_density": 140.3406,
  "population_density_1970": 37.15165197268303
}
{
  "country": "Gibraltar",
  "population_1970": 26685,
  "area_km2": 6,
  "population_density": 5441.5,
  "population_density_1970": 4447.5
}
{
  "country": "Greece",
  "population_1970": 8544873,
  "area_km2": 131990,
  "population_density": 78.68,
  "population_density_1970": 64.73879081748618
}
{
  "country": "Greenland",
  "population_1970": 45434,
  "area_km2": 2166086,
  "population_density": 0.0261,
  "population_density_1970": 0.020975159804366032
}
{
  "country": "Grenada",
  "population_1970": 98794,
  "area_km2": 344,
  "population_density": 364.6453,
  "population_density_1970": 287.1918604651163
}
{
  "country": "Guadeloupe",
  "population_1970": 318310,
  "area_km2": 1628,
  "population_density": 243.0909,
  "population_density_1970": 195.52211302211302
}
{
  "country": "Guam",
  "population_1970": 88300,
  "area_km2": 549,
  "population_density": 312.8852,
  "population_density_1970": 160.83788706739526
}
{
  "country": "Guatemala",
  "population_1970": 5453208,
  "area_km2": 108889,
  "population_density": 163.8725,
  "population_density_1970": 50.080430530172926
}
{
  "country": "Guernsey",
  "population_1970": 52656,
  "area_km2": 78,
  "population_density": 811.5513,
  "population_density_1970": 675.0769230769231
}
{
  "country": "Guinea",
  "population_1970": 4222374,
  "area_km2": 245857,
  "population_density": 56.3716,
  "population_density_1970": 17.174105272577147
}
{
  "country": "Guinea-Bissau",
  "population_1970": 591663,
  "area_km2": 36125,
  "population_density": 58.2856,
  "population_density_1970": 16.378214532871972
}
{
  "country": "Guyana",
  "population_1970": 705261,
  "area_km2": 214969,
  "population_density": 3.7621,
  "population_density_1970": 3.2807567602770633
}
{
  "country": "Haiti",
  "population_1970": 4680812,
  "area_km2": 27750,
  "population_density": 417.4773,
  "population_density_1970": 168.6779099099099
}
{
  "country": "Honduras",
  "population_1970": 2782753,
  "area_km2": 112492,
  "population_density": 92.7431,
  "population_density_1970": 24.737341322049566
}
{
  "country": "Hong Kong",
  "population_1970": 3955072,
  "area_km2": 1104,
  "population_density": 6783.3922,
  "population_density_1970": 3582.4927536231885
}
{
  "country": "Hungary",
  "population_1970": 10315366,
  "area_km2": 93028,
  "population_density": 107.1431,
  "population_density_1970": 110.88452938900116
}
{
  "country": "Iceland",
  "population_1970": 204468,
  "area_km2": 103000,
  "population_density": 3.6204,
  "population_density_1970": 1.985126213592233
}
{
  "country": "India",
  "population_1970": 557501301,
  "area_km2": 3287590,
  "population_density": 431.0675,
  "population_density_1970": 169.57750236495426
}
{
  "country": "Indonesia",
  "population_1970": 115228394,
  "area_km2": 1904569,
  "population_density": 144.6529,
  "population_density_1970": 60.50103409222769
}
{
  "country": "Iran",
  "population_1970": 28449705,
  "area_km2": 1648195,
  "population_density": 53.7258,
  "population_density_1970": 17.26112808253878
}
{
  "country": "Iraq",
  "population_1970": 9811347,
  "area_km2": 438317,
  "population_density": 101.5158,
  "population_density_1970": 22.384135226331626
}
{
  "country": "Ireland",
  "population_1970": 2937637,
  "area_km2": 70273,
  "population_density": 71.4799,
  "population_density_1970": 41.803210336829224
}
{
  "country": "Isle of Man",
  "population_1970": 55298,
  "area_km2": 572,
  "population_density": 147.7605,
  "population_density_1970": 96.67482517482517
}
{
  "country": "Israel",
  "population_1970": 2907307,
  "area_km2": 20770,
  "population_density": 435.1617,
  "population_density_1970": 139.97626384207993
}
{
  "country": "Italy",
  "population_1970": 53324036,
  "area_km2": 301336,
  "population_density": 195.9191,
  "population_density_1970": 176.9587304537128
}
{
  "country": "Ivory Coast",
  "population_1970": 5477086,
  "area_km2": 322463,
  "population_density": 87.3295,
  "population_density_1970": 16.985161088248883
}
{
  "country": "Jamaica",
  "population_1970": 1859091,
  "area_km2": 10991,
  "population_density": 257.2447,
  "population_density_1970": 169.1466654535529
}
{
  "country": "Japan",
  "population_1970": 105416839,
  "area_km2": 377930,
  "population_density": 327.9753,
  "population_density_1970": 278.932180562538
}
{
  "country": "Jersey",
  "population_1970": 68347,
  "area_km2": 116,
  "population_density": 954.9828,
  "population_density_1970": 589.198275862069
}
{
  "country": "Jordan",
  "population_1970": 1557374,
  "area_km2": 89342,
  "population_density": 126.3221,
  "population_density_1970": 17.431599919410804
}
{
  "country": "Kazakhstan",
  "population_1970": 12265305,
  "area_km2": 2724900,
  "population_density": 7.1188,
  "population_density_1970": 4.501194539249147
}
{
  "country": "Kenya",
  "population_1970": 11473087,
  "area_km2": 580367,
  "population_density": 93.0919,
  "population_density_1970": 19.768675682800712
}
{
  "country": "Kiribati",
  "population_1970": 57437,
  "area_km2": 811,
  "population_density": 161.815,
  "population_density_1970": 70.82244143033292
}
{
  "country": "Kuwait",
  "population_1970": 802786,
  "area_km2": 17818,
  "population_density": 239.5821,
  "population_density_1970": 45.054776069143564
}
{
  "country": "Kyrgyzstan",
  "population_1970": 3016384,
  "area_km2": 199951,
  "population_density": 33.1612,
  "population_density_1970": 15.085615975914099
}
{
  "country": "Laos",
  "population_1970": 2675283,
  "area_km2": 236800,
  "population_density": 31.7968,
  "population_density_1970": 11.297647804054055
}
{
  "country": "Latvia",
  "population_1970": 2397414,
  "area_km2": 64559,
  "population_density": 28.666,
  "population_density_1970": 37.13524063259964
}
{
  "country": "Lebanon",
  "population_1970": 2381791,
  "area_km2": 10452,
  "population_density": 525.2334,
  "population_density_1970": 227.87897053195562
}
{
  "country": "Lesotho",
  "population_1970": 1023481,
  "area_km2": 30355,
  "population_density": 75.962,
  "population_density_1970": 33.71704826223028
}
{
  "country": "Liberia",
  "population_1970": 1463563,
  "area_km2": 111369,
  "population_density": 47.6136,
  "population_density_1970": 13.141565426644757
}
{
  "country": "Libya",
  "population_1970": 1909177,
  "area_km2": 1759540,
  "population_density": 3.8717,
  "population_density_1970": 1.0850432499403253
}
{
  "country": "Liechtenstein",
  "population_1970": 21089,
  "area_km2": 160,
  "population_density": 245.7937,
  "population_density_1970": 131.80625
}
{
  "country": "Lithuania",
  "population_1970": 3210147,
  "area_km2": 65300,
  "population_density": 42.1142,
  "population_density_1970": 49.15998468606432
}
{
  "country": "Luxembourg",
  "population_1970": 339342,
  "area_km2": 2586,
  "population_density": 250.425,
  "population_density_1970": 131.22273781902553
}
{
  "country": "Macau",
  "population_1970": 247284,
  "area_km2": 30,
  "population_density": 23172.2667,
  "population_density_1970": 8242.8
}
{
  "country": "Madagascar",
  "population_1970": 6639751,
  "area_km2": 587041,
  "population_density": 50.4423,
  "population_density_1970": 11.310540490357573
}
{
  "country": "Malawi",
  "population_1970": 4625141,
  "area_km2": 118484,
  "population_density": 172.22,
  "population_density_1970": 39.03599642145775
}
{
  "country": "Malaysia",
  "population_1970": 10306508,
  "area_km2": 330803,
  "population_density": 102.5934,
  "population_density_1970": 31.156029419322074
}
{
  "country": "Maldives",
  "population_1970": 123243,
  "area_km2": 300,
  "population_density": 1745.9567,
  "population_density_1970": 410.81
}
{
  "country": "Mali",
  "population_1970": 6153587,
  "area_km2": 1240192,
  "population_density": 18.2178,
  "population_density_1970": 4.961801882289194
}
{
  "country": "Malta",
  "population_1970": 315414,
  "area_km2": 316,
  "population_density": 1687.6139,
  "population_density_1970": 998.1455696202531
}
{
  "country": "Marshall Islands",
  "population_1970": 23969,
  "area_km2": 181,
  "population_density": 229.663,
  "population_density_1970": 132.4254143646409
}
{
  "country": "Martinique",
  "population_1970": 326428,
  "area_km2": 1128,
  "population_density": 325.8041,
  "population_density_1970": 289.38652482269504
}
{
  "country": "Mauritania",
  "population_1970": 1122198,
  "area_km2": 1030700,
  "population_density": 4.5951,
  "population_density_1970": 1.0887726787620065
}
{
  "country": "Mauritius",
  "population_1970": 830115,
  "area_km2": 2040,
  "population_density": 636.9946,
  "population_density_1970": 406.91911764705884
}
{
  "country": "Mayotte",
  "population_1970": 35383,
  "area_km2": 374,
  "population_density": 871.9278,
  "population_density_1970": 94.60695187165776
}
{
  "country": "Mexico",
  "population_1970": 50289306,
  "area_km2": 1964375,
  "population_density": 64.9082,
  "population_density_1970": 25.600664842507157
}
{
  "country": "Micronesia",
  "population_1970": 58989,
  "area_km2": 702,
  "population_density": 162.6268,
  "population_density_1970": 84.02991452991454
}
{
  "country": "Moldova",
  "population_1970": 3711140,
  "area_km2": 33846,
  "population_density": 96.7026,
  "population_density_1970": 109.64781658098445
}
{
  "country": "Monaco",
  "population_1970": 24270,
  "area_km2": 2,
  "population_density": 18234.5,
  "population_density_1970": 12135
}
{
  "country": "Mongolia",
  "population_1970": 1293880,
  "area_km2": 1564110,
  "population_density": 2.1727,
  "population_density_1970": 0.8272308213616689
}
{
  "country": "Montenegro",
  "population_1970": 530268,
  "area_km2": 13812,
  "population_density": 45.4012,
  "population_density_1970": 38.39183318853171
}
{
  "country": "Montserrat",
  "population_1970": 11402,
  "area_km2": 102,
  "population_density": 43.0392,
  "population_density_1970": 111.7843137254902
}
{
  "country": "Morocco",
  "population_1970": 15274351,
  "area_km2": 446550,
  "population_density": 83.883,
  "population_density_1970": 34.20524241406338
}
{
  "country": "Mozambique",
  "population_1970": 8411676,
  "area_km2": 801590,
  "population_density": 41.1302,
  "population_density_1970": 10.493738694344989
}
{
  "country": "Myanmar",
  "population_1970": 27284112,
  "area_km2": 676578,
  "population_density": 80.0784,
  "population_density_1970": 40.32663196261185
}
{
  "country": "Namibia",
  "population_1970": 754467,
  "area_km2": 825615,
  "population_density": 3.1092,
  "population_density_1970": 0.9138242401119165
}
{
  "country": "Nauru",
  "population_1970": 6663,
  "area_km2": 21,
  "population_density": 603.2381,
  "population_density_1970": 317.2857142857143
}
{
  "country": "Nepal",
  "population_1970": 12501285,
  "area_km2": 147181,
  "population_density": 207.5511,
  "population_density_1970": 84.93817136722811
}
{
  "country": "Netherlands",
  "population_1970": 13037686,
  "area_km2": 41850,
  "population_density": 419.6897,
  "population_density_1970": 311.533715651135
}
{
  "country": "New Caledonia",
  "population_1970": 110982,
  "area_km2": 18575,
  "population_density": 15.6097,
  "population_density_1970": 5.974804845222073
}
{
  "country": "New Zealand",
  "population_1970": 2824061,
  "area_km2": 270467,
  "population_density": 19.1716,
  "population_density_1970": 10.441425386461194
}
{
  "country": "Nicaragua",
  "population_1970": 2444767,
  "area_km2": 130373,
  "population_density": 53.2962,
  "population_density_1970": 18.752095909429098
}
{
  "country": "Niger",
  "population_1970": 4669708,
  "area_km2": 1267000,
  "population_density": 20.6851,
  "population_density_1970": 3.6856416732438833
}
{
  "country": "Nigeria",
  "population_1970": 55569264,
  "area_km2": 923768,
  "population_density": 236.5759,
  "population_density_1970": 60.154999956699086
}
{
  "country": "Niue",
  "population_1970": 5185,
  "area_km2": 260,
  "population_density": 7.4385,
  "population_density_1970": 19.942307692307693
}
{
  "country": "North Korea",
  "population_1970": 14996879,
  "area_km2": 120538,
  "population_density": 216.2755,
  "population_density_1970": 124.41619240405515
}
{
  "country": "North Macedonia",
  "population_1970": 1656783,
  "area_km2": 25713,
  "population_density": 81.4218,
  "population_density_1970": 64.43367168358418
}
{
  "country": "Northern Mariana Islands",
  "population_1970": 10143,
  "area_km2": 464,
  "population_density": 106.7909,
  "population_density_1970": 21.85991379310345
}
{
  "country": "Norway",
  "population_1970": 3875546,
  "area_km2": 323802,
  "population_density": 16.7828,
  "population_density_1970": 11.968876041531553
}
{
  "country": "Oman",
  "population_1970": 670693,
  "area_km2": 309500,
  "population_density": 14.7861,
  "population_density_1970": 2.1670210016155087
}
{
  "country": "Pakistan",
  "population_1970": 59290872,
  "area_km2": 881912,
  "population_density": 267.4018,
  "population_density_1970": 67.22991863133737
}
{
  "country": "Palau",
  "population_1970": 11366,
  "area_km2": 459,
  "population_density": 39.3355,
  "population_density_1970": 24.762527233115467
}
{
  "country": "Palestine",
  "population_1970": 1118241,
  "area_km2": 6220,
  "population_density": 844.063,
  "population_density_1970": 179.78151125401928
}
{
  "country": "Panama",
  "population_1970": 1516188,
  "area_km2": 75417,
  "population_density": 58.4561,
  "population_density_1970": 20.104061418513066
}
{
  "country": "Papua New Guinea",
  "population_1970": 2489059,
  "area_km2": 462840,
  "population_density": 21.9139,
  "population_density_1970": 5.377795782559848
}
{
  "country": "Paraguay",
  "population_1970": 2408787,
  "area_km2": 406752,
  "population_density": 16.6705,
  "population_density_1970": 5.922004071276847
}
{
  "country": "Peru",
  "population_1970": 13562371,
  "area_km2": 1285216,
  "population_density": 26.4933,
  "population_density_1970": 10.552600496725843
}
{
  "country": "Philippines",
  "population_1970": 37435586,
  "area_km2": 342353,
  "population_density": 337.5434,
  "population_density_1970": 109.3479128268191
}
{
  "country": "Poland",
  "population_1970": 32482943,
  "area_km2": 312679,
  "population_density": 127.4698,
  "population_density_1970": 103.88591174974974
}
{
  "country": "Portugal",
  "population_1970": 8683631,
  "area_km2": 92090,
  "population_density": 111.5307,
  "population_density_1970": 94.29504832229341
}
{
  "country": "Puerto Rico",
  "population_1970": 2737619,
  "area_km2": 8870,
  "population_density": 366.675,
  "population_density_1970": 308.6379932356257
}
{
  "country": "Qatar",
  "population_1970": 118007,
  "area_km2": 11586,
  "population_density": 232.6189,
  "population_density_1970": 10.185309856723633
}
{
  "country": "Republic of the Congo",
  "population_1970": 1396989,
  "area_km2": 342000,
  "population_density": 17.4574,
  "population_density_1970": 4.084763157894737
}
{
  "country": "Reunion",
  "population_1970": 473925,
  "area_km2": 2511,
  "population_density": 387.914,
  "population_density_1970": 188.73954599761052
}
{
  "country": "Romania",
  "population_1970": 19922618,
  "area_km2": 238391,
  "population_density": 82.4665,
  "population_density_1970": 83.57118347588626
}
{
  "country": "Russia",
  "population_1970": 130093010,
  "area_km2": 17098242,
  "population_density": 8.4636,
  "population_density_1970": 7.608560575993719
}
{
  "country": "Rwanda",
  "population_1970": 3896367,
  "area_km2": 26338,
  "population_density": 523.0731,
  "population_density_1970": 147.9370870984889
}
{
  "country": "Saint Barthelemy",
  "population_1970": 2417,
  "area_km2": 21,
  "population_density": 522.2381,
  "population_density_1970": 115.0952380952381
}
{
  "country": "Saint Kitts and Nevis",
  "population_1970": 44968,
  "area_km2": 261,
  "population_density": 182.5939,
  "population_density_1970": 172.2911877394636
}
{
  "country": "Saint Lucia",
  "population_1970": 103090,
  "area_km2": 616,
  "population_density": 291.9756,
  "population_density_1970": 167.3538961038961
}
{
  "country": "Saint Martin",
  "population_1970": 5802,
  "area_km2": 53,
  "population_density": 599.8302,
  "population_density_1970": 109.47169811320755
}
{
  "country": "Saint Pierre and Miquelon",
  "population_1970": 5537,
  "area_km2": 242,
  "population_density": 24.2231,
  "population_density_1970": 22.880165289256198
}
{
  "country": "Saint Vincent and the Grenadines",
  "population_1970": 98459,
  "area_km2": 389,
  "population_density": 267.2185,
  "population_density_1970": 253.10796915167094
}
{
  "country": "Samoa",
  "population_1970": 142771,
  "area_km2": 2842,
  "population_density": 78.2484,
  "population_density_1970": 50.23610133708656
}
{
  "country": "San Marino",
  "population_1970": 18169,
  "area_km2": 61,
  "population_density": 551.8033,
  "population_density_1970": 297.8524590163934
}
{
  "country": "Sao Tome and Principe",
  "population_1970": 77583,
  "area_km2": 964,
  "population_density": 235.8714,
  "population_density_1970": 80.48029045643153
}
{
  "country": "Saudi Arabia",
  "population_1970": 6106191,
  "area_km2": 2149690,
  "population_density": 16.9368,
  "population_density_1970": 2.840498397443352
}
{
  "country": "Senegal",
  "population_1970": 4367744,
  "area_km2": 196722,
  "population_density": 88.025,
  "population_density_1970": 22.202620957493316
}
{
  "country": "Serbia",
  "population_1970": 7193533,
  "area_km2": 88361,
  "population_density": 81.7257,
  "population_density_1970": 81.41072418827311
}
{
  "country": "Seychelles",
  "population_1970": 54379,
  "area_km2": 452,
  "population_density": 236.9867,
  "population_density_1970": 120.3075221238938
}
{
  "country": "Sierra Leone",
  "population_1970": 2778557,
  "area_km2": 71740,
  "population_density": 119.957,
  "population_density_1970": 38.730931140228606
}
{
  "country": "Singapore",
  "population_1970": 2061831,
  "area_km2": 710,
  "population_density": 8416.4634,
  "population_density_1970": 2903.987323943662
}
{
  "country": "Sint Maarten",
  "population_1970": 6260,
  "area_km2": 34,
  "population_density": 1299.2647,
  "population_density_1970": 184.11764705882354
}
{
  "country": "Slovakia",
  "population_1970": 4522867,
  "area_km2": 49037,
  "population_density": 115.0856,
  "population_density_1970": 92.23376226114975
}
{
  "country": "Slovenia",
  "population_1970": 1741286,
  "area_km2": 20273,
  "population_density": 104.5649,
  "population_density_1970": 85.89187589404627
}
{
  "country": "Solomon Islands",
  "population_1970": 172833,
  "area_km2": 28896,
  "population_density": 25.0648,
  "population_density_1970": 5.981208471760797
}
{
  "country": "Somalia",
  "population_1970": 3720977,
  "area_km2": 637657,
  "population_density": 27.5971,
  "population_density_1970": 5.835389558963518
}
{
  "country": "South Africa",
  "population_1970": 22368306,
  "area_km2": 1221037,
  "population_density": 49.0517,
  "population_density_1970": 18.319105809242473
}
{
  "country": "South Korea",
  "population_1970": 32601143,
  "area_km2": 100210,
  "population_density": 517.0722,
  "population_density_1970": 325.3282406945415
}
{
  "country": "South Sudan",
  "population_1970": 3342410,
  "area_km2": 619745,
  "population_density": 17.6091,
  "population_density_1970": 5.393202042775657
}
{
  "country": "Spain",
  "population_1970": 33792617,
  "area_km2": 505992,
  "population_density": 93.9909,
  "population_density_1970": 66.7848839507344
}
{
  "country": "Sri Lanka",
  "population_1970": 12388769,
  "area_km2": 65610,
  "population_density": 332.7563,
  "population_density_1970": 188.82440176802317
}
{
  "country": "Sudan",
  "population_1970": 11305206,
  "area_km2": 1886068,
  "population_density": 24.8529,
  "population_density_1970": 5.994060659530834
}
{
  "country": "Suriname",
  "population_1970": 379918,
  "area_km2": 163820,
  "population_density": 3.7727,
  "population_density_1970": 2.3191185447442315
}
{
  "country": "Sweden",
  "population_1970": 8027702,
  "area_km2": 450295,
  "population_density": 23.4276,
  "population_density_1970": 17.82765076227806
}
{
  "country": "Switzerland",
  "population_1970": 6181227,
  "area_km2": 41284,
  "population_density": 211.7157,
  "population_density_1970": 149.72451797306462
}
{
  "country": "Syria",
  "population_1970": 6319199,
  "area_km2": 185180,
  "population_density": 119.4797,
  "population_density_1970": 34.12463008964251
}
{
  "country": "Taiwan",
  "population_1970": 14957870,
  "area_km2": 36193,
  "population_density": 660.1662,
  "population_density_1970": 413.2807448954218
}
{
  "country": "Tajikistan",
  "population_1970": 2993019,
  "area_km2": 143100,
  "population_density": 69.5513,
  "population_density_1970": 20.915576519916144
}
{
  "country": "Tanzania",
  "population_1970": 13618192,
  "area_km2": 945087,
  "population_density": 69.3034,
  "population_density_1970": 14.409458600107715
}
{
  "country": "Thailand",
  "population_1970": 35791728,
  "area_km2": 513120,
  "population_density": 139.7276,
  "population_density_1970": 69.75313376987839
}
{
  "country": "Timor-Leste",
  "population_1970": 554021,
  "area_km2": 14874,
  "population_density": 90.1772,
  "population_density_1970": 37.247613284926715
}
{
  "country": "Togo",
  "population_1970": 2197383,
  "area_km2": 56785,
  "population_density": 155.8281,
  "population_density_1970": 38.6965395791142
}
{
  "country": "Tokelau",
  "population_1970": 1714,
  "area_km2": 12,
  "population_density": 155.9167,
  "population_density_1970": 142.83333333333334
}
{
  "country": "Tonga",
  "population_1970": 86484,
  "area_km2": 747,
  "population_density": 143.0495,
  "population_density_1970": 115.77510040160642
}
{
  "country": "Trinidad and Tobago",
  "population_1970": 988890,
  "area_km2": 5130,
  "population_density": 298.4491,
  "population_density_1970": 192.76608187134502
}
{
  "country": "Tunisia",
  "population_1970": 5047404,
  "area_km2": 163610,
  "population_density": 75.5218,
  "population_density_1970": 30.850216979402237
}
{
  "country": "Turkey",
  "population_1970": 35540990,
  "area_km2": 783562,
  "population_density": 108.9145,
  "population_density_1970": 45.358235851151534
}
{
  "country": "Turkmenistan",
  "population_1970": 2201432,
  "area_km2": 488100,
  "population_density": 13.1751,
  "population_density_1970": 4.51020692481049
}
{
  "country": "Turks and Caicos Islands",
  "population_1970": 5665,
  "area_km2": 948,
  "population_density": 48.2099,
  "population_density_1970": 5.975738396624473
}
{
  "country": "Tuvalu",
  "population_1970": 5814,
  "area_km2": 26,
  "population_density": 435.0769,
  "population_density_1970": 223.6153846153846
}
{
  "country": "Uganda",
  "population_1970": 10317212,
  "area_km2": 241550,
  "population_density": 195.61,
  "population_density_1970": 42.712531566963364
}
{
  "country": "Ukraine",
  "population_1970": 47279086,
  "area_km2": 603500,
  "population_density": 65.7858,
  "population_density_1970": 78.34148467274234
}
{
  "country": "United Arab Emirates",
  "population_1970": 298084,
  "area_km2": 83600,
  "population_density": 112.9322,
  "population_density_1970": 3.565598086124402
}
{
  "country": "United Kingdom",
  "population_1970": 55650166,
  "area_km2": 242900,
  "population_density": 277.9289,
  "population_density_1970": 229.10731165088515
}
{
  "country": "United States",
  "population_1970": 200328340,
  "area_km2": 9372610,
  "population_density": 36.0935,
  "population_density_1970": 21.37380516206265
}
{
  "country": "United States Virgin Islands",
  "population_1970": 63446,
  "area_km2": 347,
  "population_density": 286.6427,
  "population_density_1970": 182.84149855907782
}
{
  "country": "Uruguay",
  "population_1970": 2790265,
  "area_km2": 181034,
  "population_density": 18.9069,
  "population_density_1970": 15.412933482108333
}
{
  "country": "Uzbekistan",
  "population_1970": 12011361,
  "area_km2": 447400,
  "population_density": 77.3975,
  "population_density_1970": 26.84702950379973
}
{
  "country": "Vanuatu",
  "population_1970": 87019,
  "area_km2": 12189,
  "population_density": 26.8061,
  "population_density_1970": 7.139141849208302
}
{
  "country": "Vatican City",
  "population_1970": 752,
  "area_km2": 1,
  "population_density": 510,
  "population_density_1970": 752
}
{
  "country": "Venezuela",
  "population_1970": 11355475,
  "area_km2": 916445,
  "population_density": 30.882,
  "population_density_1970": 12.390787226729373
}
{
  "country": "Vietnam",
  "population_1970": 41928849,
  "area_km2": 331212,
  "population_density": 296.4472,
  "population_density_1970": 126.59217963117278
}
{
  "country": "Wallis and Futuna",
  "population_1970": 9377,
  "area_km2": 142,
  "population_density": 81.493,
  "population_density_1970": 66.03521126760563
}
{
  "country": "Western Sahara",
  "population_1970": 76371,
  "area_km2": 266000,
  "population_density": 2.1654,
  "population_density_1970": 0.287109022556391
}
{
  "country": "Yemen",
  "population_1970": 6843607,
  "area_km2": 527968,
  "population_density": 63.8232,
  "population_density_1970": 12.962162479544215
}
{
  "country": "Zambia",
  "population_1970": 4281671,
  "area_km2": 752612,
  "population_density": 26.5976,
  "population_density_1970": 5.6890814921898665
}
{
  "country": "Zimbabwe",
  "population_1970": 5202918,
  "area_km2": 390757,
  "population_density": 41.7665,
  "population_density_1970": 13.31497068510609
}

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