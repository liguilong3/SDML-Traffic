# Neighborhood Selection — concrete Flow case

Time: `2016-10-11 12:55:00`; inference model: `gpt-6-luna`; K = 6.

## Developer message

```text
You estimate current urban traffic states at locations without sensors.
Target nodes have no observed states at any time. Use only the supplied
static attributes, category-level POI counts, and Seen-node observations.
Missing attributes are unknown. Return valid JSON only, with exactly the
requested target IDs and finite numerical estimates where requested.
```

## User message

```text
Task: Estimate the current state of every target node at time t.
City: Torino, Italy
Observation date: 2016-10-11
Day of week: Tuesday
Local time: 12:55:00
Nominal sampling interval: 5 minutes
State definition and unit: Traffic flow in vehicles per hour per lane; values are nonnegative.
Seen observations follow the three consecutive data columns [t-2,t-1,t], oldest to newest.
The last value is observed at the target time t. Targets provide static attributes only.
Observation timestamps: ["2016-10-11 12:45:00","2016-10-11 12:50:00","2016-10-11 12:55:00"]
DATA:
{
  "seen": [
    {
      "attributes": {
        "lanes": 3.0,
        "latitude": 45.0888,
        "longitude": 7.64708,
        "name": "Corso Regina Margherita",
        "road_class": "primary"
      },
      "id": "415",
      "observations": [
        384.0,
        372.0,
        336.0
      ],
      "poi_counts": {
        "accommodation": 20,
        "education": 0,
        "food": 0,
        "healthcare": 0,
        "other": 0,
        "recreation": 2,
        "services": 2,
        "shopping": 0,
        "transport": 1
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 25
    },
    {
      "attributes": {
        "lanes": 2.0,
        "latitude": 45.0494341,
        "longitude": 7.6324361,
        "name": "Corso Sebastopoli",
        "road_class": "secondary"
      },
      "id": "418",
      "observations": [
        312.0,
        324.0,
        228.0
      ],
      "poi_counts": {
        "accommodation": 132,
        "education": 1,
        "food": 7,
        "healthcare": 6,
        "other": 0,
        "recreation": 0,
        "services": 5,
        "shopping": 1,
        "transport": 14
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 166
    },
    {
      "attributes": {
        "lanes": 3.0,
        "latitude": 45.0338114,
        "longitude": 7.6424017,
        "name": "Corso Giovanni Agnelli",
        "road_class": "secondary"
      },
      "id": "424",
      "observations": [
        220.0,
        180.0,
        192.0
      ],
      "poi_counts": {
        "accommodation": 289,
        "education": 0,
        "food": 11,
        "healthcare": 5,
        "other": 0,
        "recreation": 0,
        "services": 8,
        "shopping": 0,
        "transport": 6
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 319
    },
    {
      "attributes": {
        "lanes": 3.0,
        "latitude": 45.0222,
        "longitude": 7.63488,
        "name": "Corso Unione Sovietica",
        "road_class": "secondary"
      },
      "id": "449",
      "observations": [
        332.0,
        272.0,
        256.0
      ],
      "poi_counts": {
        "accommodation": 65,
        "education": 0,
        "food": 16,
        "healthcare": 2,
        "other": 0,
        "recreation": 1,
        "services": 4,
        "shopping": 0,
        "transport": 20
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 108
    },
    {
      "attributes": {
        "lanes": 3.0,
        "latitude": 45.1161,
        "longitude": 7.70912,
        "name": "Corso Giulio Cesare",
        "road_class": "residential"
      },
      "id": "2012",
      "observations": [
        276.0,
        184.0,
        208.0
      ],
      "poi_counts": {
        "accommodation": 14,
        "education": 0,
        "food": 2,
        "healthcare": 2,
        "other": 0,
        "recreation": 2,
        "services": 1,
        "shopping": 0,
        "transport": 2
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 23
    },
    {
      "attributes": {
        "lanes": 2.0,
        "latitude": 45.0718659,
        "longitude": 7.706338,
        "name": "Corso Belgio",
        "road_class": "secondary"
      },
      "id": "2218",
      "observations": [
        252.0,
        324.0,
        342.0
      ],
      "poi_counts": {
        "accommodation": 130,
        "education": 6,
        "food": 30,
        "healthcare": 2,
        "other": 0,
        "recreation": 4,
        "services": 9,
        "shopping": 5,
        "transport": 11
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 197
    },
    {
      "attributes": {
        "lanes": 4.0,
        "latitude": 45.0753057,
        "longitude": 7.7047022,
        "name": "Corso Novara",
        "road_class": "secondary"
      },
      "id": "2222",
      "observations": [
        258.0,
        285.0,
        276.0
      ],
      "poi_counts": {
        "accommodation": 62,
        "education": 5,
        "food": 8,
        "healthcare": 1,
        "other": 0,
        "recreation": 6,
        "services": 5,
        "shopping": 1,
        "transport": 18
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 106
    },
    {
      "attributes": {
        "lanes": 2.0,
        "latitude": 45.0849227,
        "longitude": 7.6960397,
        "name": "Corso Novara",
        "road_class": "secondary"
      },
      "id": "2256",
      "observations": [
        276.0,
        246.0,
        276.0
      ],
      "poi_counts": {
        "accommodation": 67,
        "education": 1,
        "food": 27,
        "healthcare": 7,
        "other": 0,
        "recreation": 1,
        "services": 8,
        "shopping": 0,
        "transport": 15
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 126
    },
    {
      "attributes": {
        "lanes": 2.0,
        "latitude": 45.0867,
        "longitude": 7.70496,
        "name": "Via Bologna",
        "road_class": "secondary"
      },
      "id": "2259",
      "observations": [
        282.0,
        318.0,
        276.0
      ],
      "poi_counts": {
        "accommodation": 90,
        "education": 0,
        "food": 5,
        "healthcare": 3,
        "other": 0,
        "recreation": 0,
        "services": 1,
        "shopping": 0,
        "transport": 3
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 102
    },
    {
      "attributes": {
        "lanes": 2.0,
        "latitude": 45.0759218,
        "longitude": 7.6920666,
        "name": "Corso Regio Parco",
        "road_class": "secondary"
      },
      "id": "2289",
      "observations": [
        366.0,
        312.0,
        288.0
      ],
      "poi_counts": {
        "accommodation": 101,
        "education": 1,
        "food": 43,
        "healthcare": 5,
        "other": 0,
        "recreation": 14,
        "services": 13,
        "shopping": 3,
        "transport": 13
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 193
    },
    {
      "attributes": {
        "lanes": 1.0,
        "latitude": 45.0807,
        "longitude": 7.68618,
        "name": "Corso Giulio Cesare",
        "road_class": "tertiary"
      },
      "id": "2309",
      "observations": [
        180.0,
        264.0,
        240.0
      ],
      "poi_counts": {
        "accommodation": 113,
        "education": 0,
        "food": 37,
        "healthcare": 5,
        "other": 0,
        "recreation": 3,
        "services": 11,
        "shopping": 0,
        "transport": 7
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 176
    },
    {
      "attributes": {
        "lanes": 2.0,
        "latitude": 45.0835,
        "longitude": 7.686,
        "name": "Corso Emilia",
        "road_class": "tertiary"
      },
      "id": "2320",
      "observations": [
        210.0,
        276.0,
        198.0
      ],
      "poi_counts": {
        "accommodation": 104,
        "education": 0,
        "food": 29,
        "healthcare": 4,
        "other": 0,
        "recreation": 2,
        "services": 10,
        "shopping": 0,
        "transport": 5
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 154
    },
    {
      "attributes": {
        "lanes": 2.0,
        "latitude": 45.0971,
        "longitude": 7.67146,
        "name": "Via Stradella",
        "road_class": "tertiary"
      },
      "id": "2397",
      "observations": [
        312.0,
        234.0,
        186.0
      ],
      "poi_counts": {
        "accommodation": 149,
        "education": 0,
        "food": 20,
        "healthcare": 7,
        "other": 0,
        "recreation": 0,
        "services": 7,
        "shopping": 1,
        "transport": 6
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 190
    },
    {
      "attributes": {
        "lanes": 2.0,
        "latitude": 45.0963,
        "longitude": 7.67222,
        "name": "Via Stradella",
        "road_class": "tertiary"
      },
      "id": "2399",
      "observations": [
        258.0,
        258.0,
        198.0
      ],
      "poi_counts": {
        "accommodation": 146,
        "education": 1,
        "food": 19,
        "healthcare": 6,
        "other": 0,
        "recreation": 0,
        "services": 6,
        "shopping": 1,
        "transport": 8
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 187
    },
    {
      "attributes": {
        "lanes": 3.0,
        "latitude": 45.0887,
        "longitude": 7.6885,
        "name": "Corso Novara",
        "road_class": "other"
      },
      "id": "2420",
      "observations": [
        152.0,
        200.0,
        204.0
      ],
      "poi_counts": {
        "accommodation": 65,
        "education": 0,
        "food": 25,
        "healthcare": 7,
        "other": 0,
        "recreation": 1,
        "services": 7,
        "shopping": 0,
        "transport": 51
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 156
    },
    {
      "attributes": {
        "lanes": 2.0,
        "latitude": 45.088,
        "longitude": 7.69046,
        "name": "Corso Novara",
        "road_class": "secondary"
      },
      "id": "2423",
      "observations": [
        432.0,
        246.0,
        378.0
      ],
      "poi_counts": {
        "accommodation": 74,
        "education": 2,
        "food": 27,
        "healthcare": 5,
        "other": 0,
        "recreation": 0,
        "services": 5,
        "shopping": 0,
        "transport": 31
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 144
    },
    {
      "attributes": {
        "lanes": 2.0,
        "latitude": 45.0876588,
        "longitude": 7.6910531,
        "name": "Corso Novara",
        "road_class": "secondary"
      },
      "id": "2425",
      "observations": [
        360.0,
        252.0,
        408.0
      ],
      "poi_counts": {
        "accommodation": 69,
        "education": 2,
        "food": 24,
        "healthcare": 5,
        "other": 0,
        "recreation": 0,
        "services": 6,
        "shopping": 0,
        "transport": 18
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 124
    },
    {
      "attributes": {
        "lanes": 2.0,
        "latitude": 45.0862,
        "longitude": 7.69369,
        "name": "Corso Novara",
        "road_class": "secondary"
      },
      "id": "2432",
      "observations": [
        336.0,
        210.0,
        318.0
      ],
      "poi_counts": {
        "accommodation": 63,
        "education": 1,
        "food": 26,
        "healthcare": 5,
        "other": 0,
        "recreation": 0,
        "services": 6,
        "shopping": 0,
        "transport": 10
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 111
    },
    {
      "attributes": {
        "lanes": 2.0,
        "latitude": 45.0847,
        "longitude": 7.69613,
        "name": "Corso Novara",
        "road_class": "secondary"
      },
      "id": "2433",
      "observations": [
        270.0,
        276.0,
        258.0
      ],
      "poi_counts": {
        "accommodation": 70,
        "education": 1,
        "food": 30,
        "healthcare": 6,
        "other": 0,
        "recreation": 1,
        "services": 8,
        "shopping": 0,
        "transport": 14
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 130
    },
    {
      "attributes": {
        "lanes": 2.0,
        "latitude": 45.0868473,
        "longitude": 7.6927891,
        "name": "Corso Novara",
        "road_class": "other"
      },
      "id": "2437",
      "observations": [
        288.0,
        222.0,
        390.0
      ],
      "poi_counts": {
        "accommodation": 63,
        "education": 2,
        "food": 19,
        "healthcare": 4,
        "other": 0,
        "recreation": 0,
        "services": 6,
        "shopping": 0,
        "transport": 9
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 103
    },
    {
      "attributes": {
        "lanes": 3.0,
        "latitude": 45.1045,
        "longitude": 7.70155,
        "name": "Corso Giulio Cesare",
        "road_class": "primary"
      },
      "id": "2467",
      "observations": [
        360.0,
        272.0,
        292.0
      ],
      "poi_counts": {
        "accommodation": 57,
        "education": 0,
        "food": 10,
        "healthcare": 3,
        "other": 0,
        "recreation": 0,
        "services": 2,
        "shopping": 0,
        "transport": 2
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 74
    },
    {
      "attributes": {
        "lanes": 4.0,
        "latitude": 45.1043546,
        "longitude": 7.6811166,
        "name": "Corso Grosseto",
        "road_class": "primary"
      },
      "id": "2494",
      "observations": [
        246.0,
        342.0,
        288.0
      ],
      "poi_counts": {
        "accommodation": 28,
        "education": 0,
        "food": 1,
        "healthcare": 4,
        "other": 0,
        "recreation": 0,
        "services": 1,
        "shopping": 0,
        "transport": 4
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 38
    },
    {
      "attributes": {
        "lanes": 4.0,
        "latitude": 45.1041792,
        "longitude": 7.6845227,
        "name": "Corso Grosseto",
        "road_class": "primary"
      },
      "id": "2498",
      "observations": [
        267.0,
        372.0,
        318.0
      ],
      "poi_counts": {
        "accommodation": 17,
        "education": 0,
        "food": 0,
        "healthcare": 2,
        "other": 0,
        "recreation": 0,
        "services": 1,
        "shopping": 0,
        "transport": 3
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 23
    },
    {
      "attributes": {
        "lanes": 2.0,
        "latitude": 45.1044,
        "longitude": 7.68489,
        "name": "Via Ala di Stura",
        "road_class": "tertiary"
      },
      "id": "2499",
      "observations": [
        492.0,
        402.0,
        270.0
      ],
      "poi_counts": {
        "accommodation": 16,
        "education": 0,
        "food": 0,
        "healthcare": 2,
        "other": 0,
        "recreation": 0,
        "services": 1,
        "shopping": 0,
        "transport": 3
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 22
    },
    {
      "attributes": {
        "lanes": 2.0,
        "latitude": 45.0457,
        "longitude": 7.64497,
        "name": "Corso Orbassano",
        "road_class": "tertiary"
      },
      "id": "2535",
      "observations": [
        414.0,
        282.0,
        336.0
      ],
      "poi_counts": {
        "accommodation": 430,
        "education": 0,
        "food": 33,
        "healthcare": 9,
        "other": 0,
        "recreation": 0,
        "services": 16,
        "shopping": 0,
        "transport": 15
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 503
    },
    {
      "attributes": {
        "lanes": 3.0,
        "latitude": 45.0221,
        "longitude": 7.65069,
        "name": "Via Pio VII",
        "road_class": "tertiary"
      },
      "id": "2563",
      "observations": [
        200.0,
        264.0,
        224.0
      ],
      "poi_counts": {
        "accommodation": 127,
        "education": 2,
        "food": 19,
        "healthcare": 7,
        "other": 0,
        "recreation": 0,
        "services": 5,
        "shopping": 0,
        "transport": 24
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 184
    },
    {
      "attributes": {
        "lanes": 3.0,
        "latitude": 45.0178,
        "longitude": 7.66176,
        "name": "Via Nizza",
        "road_class": "secondary"
      },
      "id": "2692",
      "observations": [
        132.0,
        208.0,
        232.0
      ],
      "poi_counts": {
        "accommodation": 110,
        "education": 0,
        "food": 19,
        "healthcare": 2,
        "other": 0,
        "recreation": 1,
        "services": 9,
        "shopping": 1,
        "transport": 13
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 155
    },
    {
      "attributes": {
        "lanes": 4.0,
        "latitude": 45.0316,
        "longitude": 7.61537,
        "name": "Corso Orbassano",
        "road_class": "primary_link"
      },
      "id": "2810",
      "observations": [
        405.0,
        366.0,
        432.0
      ],
      "poi_counts": {
        "accommodation": 6,
        "education": 0,
        "food": 4,
        "healthcare": 0,
        "other": 0,
        "recreation": 0,
        "services": 0,
        "shopping": 0,
        "transport": 4
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 14
    },
    {
      "attributes": {
        "lanes": 3.0,
        "latitude": 45.0232981,
        "longitude": 7.6352983,
        "name": "Corso Giovanni Agnelli",
        "road_class": "secondary"
      },
      "id": "2823",
      "observations": [
        252.0,
        212.0,
        264.0
      ],
      "poi_counts": {
        "accommodation": 66,
        "education": 0,
        "food": 17,
        "healthcare": 2,
        "other": 0,
        "recreation": 1,
        "services": 5,
        "shopping": 0,
        "transport": 16
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 107
    },
    {
      "attributes": {
        "lanes": 3.0,
        "latitude": 45.0307209,
        "longitude": 7.6402861,
        "name": "Corso Giovanni Agnelli",
        "road_class": "secondary"
      },
      "id": "2840",
      "observations": [
        196.0,
        208.0,
        132.0
      ],
      "poi_counts": {
        "accommodation": 108,
        "education": 0,
        "food": 6,
        "healthcare": 2,
        "other": 0,
        "recreation": 0,
        "services": 5,
        "shopping": 0,
        "transport": 7
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 128
    },
    {
      "attributes": {
        "lanes": 2.0,
        "latitude": 45.0346417,
        "longitude": 7.6281041,
        "name": "Corso Enrico Tazzoli",
        "road_class": "tertiary"
      },
      "id": "2843",
      "observations": [
        354.0,
        312.0,
        270.0
      ],
      "poi_counts": {
        "accommodation": 71,
        "education": 0,
        "food": 4,
        "healthcare": 2,
        "other": 0,
        "recreation": 2,
        "services": 4,
        "shopping": 0,
        "transport": 9
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 92
    },
    {
      "attributes": {
        "lanes": 3.0,
        "latitude": 45.0409,
        "longitude": 7.63407,
        "name": "Corso Siracusa",
        "road_class": "primary"
      },
      "id": "2855",
      "observations": [
        328.0,
        352.0,
        284.0
      ],
      "poi_counts": {
        "accommodation": 235,
        "education": 0,
        "food": 9,
        "healthcare": 6,
        "other": 0,
        "recreation": 0,
        "services": 5,
        "shopping": 0,
        "transport": 16
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 271
    },
    {
      "attributes": {
        "lanes": 3.0,
        "latitude": 45.035826,
        "longitude": 7.6409877,
        "name": "Corso Cosenza",
        "road_class": "primary"
      },
      "id": "2863",
      "observations": [
        412.0,
        256.0,
        352.0
      ],
      "poi_counts": {
        "accommodation": 349,
        "education": 0,
        "food": 14,
        "healthcare": 7,
        "other": 0,
        "recreation": 0,
        "services": 4,
        "shopping": 0,
        "transport": 9
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 383
    },
    {
      "attributes": {
        "lanes": 3.0,
        "latitude": 45.0362848,
        "longitude": 7.6406632,
        "name": "Corso Cosenza",
        "road_class": "primary"
      },
      "id": "2864",
      "observations": [
        460.0,
        344.0,
        372.0
      ],
      "poi_counts": {
        "accommodation": 350,
        "education": 0,
        "food": 15,
        "healthcare": 7,
        "other": 0,
        "recreation": 0,
        "services": 4,
        "shopping": 0,
        "transport": 9
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 385
    },
    {
      "attributes": {
        "lanes": 3.0,
        "latitude": 45.0492773,
        "longitude": 7.6336493,
        "name": "Corso Sebastopoli",
        "road_class": "secondary"
      },
      "id": "2882",
      "observations": [
        216.0,
        208.0,
        216.0
      ],
      "poi_counts": {
        "accommodation": 148,
        "education": 1,
        "food": 9,
        "healthcare": 6,
        "other": 0,
        "recreation": 2,
        "services": 6,
        "shopping": 1,
        "transport": 15
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 188
    },
    {
      "attributes": {
        "lanes": 3.0,
        "latitude": 45.0485,
        "longitude": 7.63428,
        "name": "Corso Siracusa",
        "road_class": "other"
      },
      "id": "2884",
      "observations": [
        372.0,
        384.0,
        332.0
      ],
      "poi_counts": {
        "accommodation": 191,
        "education": 1,
        "food": 9,
        "healthcare": 6,
        "other": 0,
        "recreation": 3,
        "services": 8,
        "shopping": 1,
        "transport": 17
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 236
    },
    {
      "attributes": {
        "lanes": 2.0,
        "latitude": 45.0532,
        "longitude": 7.6694,
        "name": "Corso Filippo Turati",
        "road_class": "secondary"
      },
      "id": "2981",
      "observations": [
        204.0,
        204.0,
        102.0
      ],
      "poi_counts": {
        "accommodation": 258,
        "education": 0,
        "food": 27,
        "healthcare": 6,
        "other": 0,
        "recreation": 2,
        "services": 14,
        "shopping": 7,
        "transport": 26
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 340
    },
    {
      "attributes": {
        "lanes": 2.0,
        "latitude": 45.0377,
        "longitude": 7.64494,
        "name": "Corso Giovanni Agnelli",
        "road_class": "other"
      },
      "id": "3000",
      "observations": [
        348.0,
        306.0,
        342.0
      ],
      "poi_counts": {
        "accommodation": 311,
        "education": 0,
        "food": 20,
        "healthcare": 6,
        "other": 0,
        "recreation": 0,
        "services": 6,
        "shopping": 0,
        "transport": 9
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 352
    },
    {
      "attributes": {
        "lanes": 2.0,
        "latitude": 45.0847,
        "longitude": 7.65944,
        "name": "Corso Regina Margherita",
        "road_class": "primary"
      },
      "id": "3059",
      "observations": [
        402.0,
        318.0,
        354.0
      ],
      "poi_counts": {
        "accommodation": 343,
        "education": 0,
        "food": 22,
        "healthcare": 7,
        "other": 0,
        "recreation": 1,
        "services": 9,
        "shopping": 0,
        "transport": 3
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 385
    },
    {
      "attributes": {
        "lanes": 3.0,
        "latitude": 45.1003,
        "longitude": 7.66007,
        "name": "Corso Potenza",
        "road_class": "primary"
      },
      "id": "3077",
      "observations": [
        296.0,
        396.0,
        168.0
      ],
      "poi_counts": {
        "accommodation": 26,
        "education": 2,
        "food": 2,
        "healthcare": 7,
        "other": 0,
        "recreation": 0,
        "services": 2,
        "shopping": 0,
        "transport": 1
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 40
    },
    {
      "attributes": {
        "lanes": 2.0,
        "latitude": 45.0587,
        "longitude": 7.66474,
        "name": "Corso Luigi Einaudi",
        "road_class": "other"
      },
      "id": "3119",
      "observations": [
        516.0,
        414.0,
        426.0
      ],
      "poi_counts": {
        "accommodation": 454,
        "education": 1,
        "food": 25,
        "healthcare": 4,
        "other": 0,
        "recreation": 0,
        "services": 10,
        "shopping": 6,
        "transport": 23
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 523
    },
    {
      "attributes": {
        "lanes": 2.0,
        "latitude": 45.0241209,
        "longitude": 7.6367732,
        "name": "Corso Unione Sovietica",
        "road_class": "secondary"
      },
      "id": "3125",
      "observations": [
        348.0,
        282.0,
        228.0
      ],
      "poi_counts": {
        "accommodation": 82,
        "education": 0,
        "food": 21,
        "healthcare": 3,
        "other": 1,
        "recreation": 1,
        "services": 6,
        "shopping": 0,
        "transport": 17
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 131
    },
    {
      "attributes": {
        "lanes": 4.0,
        "latitude": 45.0526,
        "longitude": 7.65556,
        "name": "Largo Orbassano",
        "road_class": "secondary"
      },
      "id": "3167",
      "observations": [
        327.0,
        354.0,
        261.0
      ],
      "poi_counts": {
        "accommodation": 223,
        "education": 0,
        "food": 57,
        "healthcare": 4,
        "other": 0,
        "recreation": 3,
        "services": 16,
        "shopping": 2,
        "transport": 21
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 326
    },
    {
      "attributes": {
        "lanes": 3.0,
        "latitude": 45.0386,
        "longitude": 7.62881,
        "name": "Via Guido Reni",
        "road_class": "secondary"
      },
      "id": "3177",
      "observations": [
        192.0,
        272.0,
        204.0
      ],
      "poi_counts": {
        "accommodation": 144,
        "education": 0,
        "food": 7,
        "healthcare": 4,
        "other": 0,
        "recreation": 3,
        "services": 3,
        "shopping": 0,
        "transport": 10
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 171
    },
    {
      "attributes": {
        "lanes": 3.0,
        "latitude": 45.0591773,
        "longitude": 7.6562244,
        "name": "Corso Mediterraneo",
        "road_class": "secondary"
      },
      "id": "3217",
      "observations": [
        488.0,
        560.0,
        448.0
      ],
      "poi_counts": {
        "accommodation": 347,
        "education": 3,
        "food": 33,
        "healthcare": 3,
        "other": 0,
        "recreation": 4,
        "services": 8,
        "shopping": 1,
        "transport": 27
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 426
    },
    {
      "attributes": {
        "lanes": 3.0,
        "latitude": 45.0727763,
        "longitude": 7.641371,
        "name": "Corso Trapani",
        "road_class": "primary"
      },
      "id": "3240",
      "observations": [
        248.0,
        196.0,
        192.0
      ],
      "poi_counts": {
        "accommodation": 517,
        "education": 0,
        "food": 27,
        "healthcare": 5,
        "other": 0,
        "recreation": 2,
        "services": 9,
        "shopping": 0,
        "transport": 15
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 575
    },
    {
      "attributes": {
        "lanes": 3.0,
        "latitude": 45.1089962,
        "longitude": 7.7048602,
        "name": "Corso Giulio Cesare",
        "road_class": "primary"
      },
      "id": "3246",
      "observations": [
        320.0,
        296.0,
        236.0
      ],
      "poi_counts": {
        "accommodation": 90,
        "education": 0,
        "food": 1,
        "healthcare": 0,
        "other": 0,
        "recreation": 0,
        "services": 0,
        "shopping": 0,
        "transport": 0
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 91
    },
    {
      "attributes": {
        "lanes": 3.0,
        "latitude": 45.0464455,
        "longitude": 7.6343812,
        "name": "Corso Siracusa",
        "road_class": "primary"
      },
      "id": "3275",
      "observations": [
        456.0,
        300.0,
        400.0
      ],
      "poi_counts": {
        "accommodation": 226,
        "education": 0,
        "food": 8,
        "healthcare": 7,
        "other": 0,
        "recreation": 0,
        "services": 9,
        "shopping": 0,
        "transport": 20
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 270
    },
    {
      "attributes": {
        "lanes": 3.0,
        "latitude": 45.0453829,
        "longitude": 7.6341563,
        "name": "Corso Siracusa",
        "road_class": "primary"
      },
      "id": "3276",
      "observations": [
        344.0,
        312.0,
        396.0
      ],
      "poi_counts": {
        "accommodation": 226,
        "education": 0,
        "food": 8,
        "healthcare": 6,
        "other": 0,
        "recreation": 0,
        "services": 9,
        "shopping": 0,
        "transport": 19
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 268
    },
    {
      "attributes": {
        "lanes": 3.0,
        "latitude": 45.0427,
        "longitude": 7.63394,
        "name": "Corso Siracusa",
        "road_class": "residential"
      },
      "id": "3285",
      "observations": [
        332.0,
        316.0,
        372.0
      ],
      "poi_counts": {
        "accommodation": 204,
        "education": 0,
        "food": 7,
        "healthcare": 8,
        "other": 0,
        "recreation": 0,
        "services": 5,
        "shopping": 0,
        "transport": 19
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 243
    },
    {
      "attributes": {
        "lanes": 2.0,
        "latitude": 45.1012735,
        "longitude": 7.660809,
        "name": "Corso Potenza",
        "road_class": "primary"
      },
      "id": "3368",
      "observations": [
        330.0,
        372.0,
        234.0
      ],
      "poi_counts": {
        "accommodation": 44,
        "education": 2,
        "food": 5,
        "healthcare": 5,
        "other": 0,
        "recreation": 0,
        "services": 6,
        "shopping": 0,
        "transport": 0
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 62
    },
    {
      "attributes": {
        "lanes": 2.0,
        "latitude": 45.0493,
        "longitude": 7.65057,
        "name": "Via Caprera",
        "road_class": "residential"
      },
      "id": "3381",
      "observations": [
        396.0,
        324.0,
        348.0
      ],
      "poi_counts": {
        "accommodation": 226,
        "education": 0,
        "food": 30,
        "healthcare": 2,
        "other": 0,
        "recreation": 1,
        "services": 16,
        "shopping": 0,
        "transport": 17
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 292
    },
    {
      "attributes": {
        "lanes": 2.0,
        "latitude": 45.041,
        "longitude": 7.63568,
        "name": "Corso Orbassano",
        "road_class": "secondary"
      },
      "id": "3388",
      "observations": [
        366.0,
        288.0,
        288.0
      ],
      "poi_counts": {
        "accommodation": 246,
        "education": 0,
        "food": 11,
        "healthcare": 7,
        "other": 0,
        "recreation": 0,
        "services": 6,
        "shopping": 0,
        "transport": 14
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 284
    },
    {
      "attributes": {
        "lanes": 2.0,
        "latitude": 45.0419,
        "longitude": 7.63786,
        "name": "Corso Orbassano",
        "road_class": "secondary"
      },
      "id": "3390",
      "observations": [
        444.0,
        378.0,
        318.0
      ],
      "poi_counts": {
        "accommodation": 254,
        "education": 0,
        "food": 14,
        "healthcare": 9,
        "other": 0,
        "recreation": 0,
        "services": 11,
        "shopping": 0,
        "transport": 14
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 302
    },
    {
      "attributes": {
        "lanes": 2.0,
        "latitude": 45.0206,
        "longitude": 7.65451,
        "name": "Corso Traiano",
        "road_class": "secondary"
      },
      "id": "3393",
      "observations": [
        444.0,
        294.0,
        426.0
      ],
      "poi_counts": {
        "accommodation": 128,
        "education": 0,
        "food": 22,
        "healthcare": 5,
        "other": 0,
        "recreation": 1,
        "services": 3,
        "shopping": 0,
        "transport": 26
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 185
    }
  ],
  "targets": [
    {
      "attributes": {
        "lanes": 2.0,
        "latitude": 45.0794,
        "longitude": 7.70075,
        "name": "Corso Novara",
        "road_class": "secondary"
      },
      "id": "2263",
      "poi_counts": {
        "accommodation": 13,
        "education": 0,
        "food": 15,
        "healthcare": 2,
        "other": 0,
        "recreation": 3,
        "services": 4,
        "shopping": 0,
        "transport": 13
      },
      "poi_scope": "existing factual graph associations",
      "poi_total": 50
    }
  ],
  "time_index": 1787
}
For each target, select exactly 6 distinct nodes from DATA.seen whose
current traffic states are expected to be most similar to that target's
current state. Consider static attributes, spatial context, POI composition,
and observed dynamics. List selected nodes in decreasing order of expected
similarity.
Neighbor IDs must come only from DATA.seen; never select any ID in DATA.targets.
Return exactly a JSON object of this form:
{"neighbors": {"target_id": ["seen_id_1", "seen_id_2"]}}
Every list must contain exactly 6 IDs; the example is schematic.
```

