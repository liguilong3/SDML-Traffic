# Rag — concrete Flow case

Time: `2016-10-11 12:55:00`; inference model: `gpt-6-luna`; K = 6.

References were retrieved using `text-embedding-3-large` from the same provider.

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
  "reference_ids": {
    "2263": [
      "2433",
      "2432",
      "2423",
      "2256",
      "2425",
      "2222"
    ]
  },
  "seen": [
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
Each target has 6 reference Seen nodes retrieved using cosine similarity
between static semantic embeddings. DATA.reference_ids maps every target
to its references, ordered by decreasing similarity. DATA.seen is the
deduplicated reference table shared by this batch.
Use the target's static attributes and its assigned references' attributes,
POI counts, and observations to estimate its current state at t.
Do not choose replacement references.
Return exactly a JSON object of this form:
{"predictions": {"target_id": 0.0}}
Return every target once, in the stated unit and valid range.
```

