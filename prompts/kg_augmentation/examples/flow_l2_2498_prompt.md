# flow_l2_2498: complete presentation example

## Instructions

Use only the supplied evidence and fixed output schema. Distinguish provided facts from semantic interpretations. Return supported values with evidence references and concise rationales. Abstain when evidence is insufficient. Do not use traffic states, occupancy histories, downstream results, or invented connections. Accepted judgments require human review before integration.

Using the target attributes, directly associated POIs, native types, and accepted L1 functions, select up to three FunctionalAreaType values. Explain and cite the evidence for each value, or abstain. Counts do not select labels automatically. Return target_id, labels, label_rationales, label_evidence, and abstention reasons.

## Allowed relations and values

```json
{
  "located_in_functional_area": {
    "level": "L2",
    "head_type": "Detid",
    "tail_type": "FunctionalAreaType",
    "allowed_values": [
      "FunctionalAreaType:Residential",
      "FunctionalAreaType:WorkStudy",
      "FunctionalAreaType:CommercialService",
      "FunctionalAreaType:MedicalHealth",
      "FunctionalAreaType:CultureLeisure",
      "FunctionalAreaType:AdministrativePublicService",
      "FunctionalAreaType:Tourism",
      "FunctionalAreaType:IndustrialLogistics",
      "FunctionalAreaType:Transport",
      "FunctionalAreaType:MixedUse"
    ],
    "max_values_per_head": 3,
    "meaning": "Inferred functional type of the surrounding area, supported by direct local evidence. No geographic area boundary is introduced."
  }
}
```

## Concrete input

```json
{
  "scene": "flow",
  "level": "L2",
  "output_schema": {
    "located_in_functional_area": {
      "level": "L2",
      "head_type": "Detid",
      "tail_type": "FunctionalAreaType",
      "allowed_values": [
        "FunctionalAreaType:Residential",
        "FunctionalAreaType:WorkStudy",
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:MedicalHealth",
        "FunctionalAreaType:CultureLeisure",
        "FunctionalAreaType:AdministrativePublicService",
        "FunctionalAreaType:Tourism",
        "FunctionalAreaType:IndustrialLogistics",
        "FunctionalAreaType:Transport",
        "FunctionalAreaType:MixedUse"
      ],
      "max_values_per_head": 3,
      "meaning": "Inferred functional type of the surrounding area, supported by direct local evidence. No geographic area boundary is introduced."
    }
  },
  "target_id": "2498",
  "target_attributes": {
    "citycode": "torino",
    "detid": "2498",
    "fclass": "primary",
    "lanes": "4.0",
    "lat": "45.1041792",
    "length": "0.243986480140569",
    "limit": "0",
    "linkid": "332.0",
    "long": "7.6845227",
    "pos": "0.228298871105118",
    "road": "Corso Grosseto"
  },
  "direct_pois": [
    {
      "poi_id": "-167015105",
      "native_types": [
        "OSM_POI_Type:place_of_worship"
      ],
      "functions": [
        "Function:PublicService"
      ],
      "association_fact": [
        "2498",
        "nearby_poi",
        "-167015105"
      ]
    },
    {
      "poi_id": "133393919",
      "native_types": [
        "OSM_POI_Type:apartments"
      ],
      "functions": [
        "Function:Residential"
      ],
      "association_fact": [
        "2498",
        "nearby_poi",
        "133393919"
      ]
    },
    {
      "poi_id": "1556869864",
      "native_types": [
        "OSM_POI_Type:fuel"
      ],
      "functions": [
        "Function:VehicleSupport"
      ],
      "association_fact": [
        "2498",
        "nearby_poi",
        "1556869864"
      ]
    },
    {
      "poi_id": "1997706758",
      "native_types": [
        "OSM_POI_Type:parking_entrance"
      ],
      "functions": [
        "Function:VehicleSupport"
      ],
      "association_fact": [
        "2498",
        "nearby_poi",
        "1997706758"
      ]
    },
    {
      "poi_id": "1997739404",
      "native_types": [
        "OSM_POI_Type:parking_entrance"
      ],
      "functions": [
        "Function:VehicleSupport"
      ],
      "association_fact": [
        "2498",
        "nearby_poi",
        "1997739404"
      ]
    },
    {
      "poi_id": "438952587",
      "native_types": [
        "OSM_POI_Type:pharmacy"
      ],
      "functions": [
        "Function:MedicalHealth"
      ],
      "association_fact": [
        "2498",
        "nearby_poi",
        "438952587"
      ]
    },
    {
      "poi_id": "439009318",
      "native_types": [
        "OSM_POI_Type:pharmacy"
      ],
      "functions": [
        "Function:MedicalHealth"
      ],
      "association_fact": [
        "2498",
        "nearby_poi",
        "439009318"
      ]
    },
    {
      "poi_id": "551096920",
      "native_types": [
        "OSM_POI_Type:apartments"
      ],
      "functions": [
        "Function:Residential"
      ],
      "association_fact": [
        "2498",
        "nearby_poi",
        "551096920"
      ]
    },
    {
      "poi_id": "551096925",
      "native_types": [
        "OSM_POI_Type:apartments"
      ],
      "functions": [
        "Function:Residential"
      ],
      "association_fact": [
        "2498",
        "nearby_poi",
        "551096925"
      ]
    },
    {
      "poi_id": "551097831",
      "native_types": [
        "OSM_POI_Type:apartments"
      ],
      "functions": [
        "Function:Residential"
      ],
      "association_fact": [
        "2498",
        "nearby_poi",
        "551097831"
      ]
    },
    {
      "poi_id": "551097832",
      "native_types": [
        "OSM_POI_Type:apartments"
      ],
      "functions": [
        "Function:Residential"
      ],
      "association_fact": [
        "2498",
        "nearby_poi",
        "551097832"
      ]
    },
    {
      "poi_id": "878127530",
      "native_types": [
        "OSM_POI_Type:apartments"
      ],
      "functions": [
        "Function:Residential"
      ],
      "association_fact": [
        "2498",
        "nearby_poi",
        "878127530"
      ]
    },
    {
      "poi_id": "878127531",
      "native_types": [
        "OSM_POI_Type:apartments"
      ],
      "functions": [
        "Function:Residential"
      ],
      "association_fact": [
        "2498",
        "nearby_poi",
        "878127531"
      ]
    },
    {
      "poi_id": "935560584",
      "native_types": [
        "OSM_POI_Type:apartments"
      ],
      "functions": [
        "Function:Residential"
      ],
      "association_fact": [
        "2498",
        "nearby_poi",
        "935560584"
      ]
    },
    {
      "poi_id": "935560585",
      "native_types": [
        "OSM_POI_Type:apartments"
      ],
      "functions": [
        "Function:Residential"
      ],
      "association_fact": [
        "2498",
        "nearby_poi",
        "935560585"
      ]
    },
    {
      "poi_id": "935560586",
      "native_types": [
        "OSM_POI_Type:apartments"
      ],
      "functions": [
        "Function:Residential"
      ],
      "association_fact": [
        "2498",
        "nearby_poi",
        "935560586"
      ]
    },
    {
      "poi_id": "935560587",
      "native_types": [
        "OSM_POI_Type:apartments"
      ],
      "functions": [
        "Function:Residential"
      ],
      "association_fact": [
        "2498",
        "nearby_poi",
        "935560587"
      ]
    },
    {
      "poi_id": "935560588",
      "native_types": [
        "OSM_POI_Type:apartments"
      ],
      "functions": [
        "Function:Residential"
      ],
      "association_fact": [
        "2498",
        "nearby_poi",
        "935560588"
      ]
    },
    {
      "poi_id": "935560589",
      "native_types": [
        "OSM_POI_Type:apartments"
      ],
      "functions": [
        "Function:Residential"
      ],
      "association_fact": [
        "2498",
        "nearby_poi",
        "935560589"
      ]
    },
    {
      "poi_id": "935560590",
      "native_types": [
        "OSM_POI_Type:apartments"
      ],
      "functions": [
        "Function:Residential"
      ],
      "association_fact": [
        "2498",
        "nearby_poi",
        "935560590"
      ]
    },
    {
      "poi_id": "935560594",
      "native_types": [
        "OSM_POI_Type:apartments"
      ],
      "functions": [
        "Function:Residential"
      ],
      "association_fact": [
        "2498",
        "nearby_poi",
        "935560594"
      ]
    },
    {
      "poi_id": "938815094",
      "native_types": [
        "OSM_POI_Type:apartments"
      ],
      "functions": [
        "Function:Residential"
      ],
      "association_fact": [
        "2498",
        "nearby_poi",
        "938815094"
      ]
    },
    {
      "poi_id": "938815095",
      "native_types": [
        "OSM_POI_Type:apartments"
      ],
      "functions": [
        "Function:Residential"
      ],
      "association_fact": [
        "2498",
        "nearby_poi",
        "938815095"
      ]
    }
  ]
}
```
