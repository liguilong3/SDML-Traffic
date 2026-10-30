# flow_l3_2498: complete presentation example

## Instructions

Use only the supplied evidence and fixed output schema. Distinguish provided facts from semantic interpretations. Return supported values with evidence references and concise rationales. Abstain when evidence is insufficient. Do not use traffic states, occupancy histories, downstream results, or invented connections. Accepted judgments require human review before integration.

Using actual directed paths, accepted L2 contexts along them, road attributes, and the target position, select one NetworkRole or abstain. Cite paths and the L2 evidence actually used. Reachability, road class, or path length alone is insufficient. Do not infer observed vehicle movements or trips.

## Allowed relations and values

```json
{
  "has_network_role": {
    "level": "L3",
    "head_type": "Detid",
    "tail_type": "NetworkRole",
    "allowed_values": [
      "NetworkRole:BackboneCorridor",
      "NetworkRole:TransitionConnector",
      "NetworkRole:LocalDistributor"
    ],
    "max_values_per_head": 1,
    "meaning": "Role within the supplied directed road-node KG, inferred jointly from paths, functions, road attributes, and target position."
  }
}
```

## Concrete input

```json
{
  "scene": "flow",
  "level": "L3",
  "output_schema": {
    "has_network_role": {
      "level": "L3",
      "head_type": "Detid",
      "tail_type": "NetworkRole",
      "allowed_values": [
        "NetworkRole:BackboneCorridor",
        "NetworkRole:TransitionConnector",
        "NetworkRole:LocalDistributor"
      ],
      "max_values_per_head": 1,
      "meaning": "Role within the supplied directed road-node KG, inferred jointly from paths, functions, road attributes, and target position."
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
  "directed_edges": [
    [
      "2012",
      "2467"
    ],
    [
      "2218",
      "3025"
    ],
    [
      "2222",
      "2218"
    ],
    [
      "2222",
      "2263"
    ],
    [
      "2222",
      "3025"
    ],
    [
      "2256",
      "2263"
    ],
    [
      "2256",
      "2289"
    ],
    [
      "2256",
      "2432"
    ],
    [
      "2259",
      "2263"
    ],
    [
      "2259",
      "2433"
    ],
    [
      "2263",
      "2218"
    ],
    [
      "2263",
      "2222"
    ],
    [
      "2289",
      "2218"
    ],
    [
      "2289",
      "2222"
    ],
    [
      "2289",
      "2263"
    ],
    [
      "2289",
      "3025"
    ],
    [
      "2309",
      "2289"
    ],
    [
      "2309",
      "2320"
    ],
    [
      "2309",
      "2423"
    ],
    [
      "2309",
      "2425"
    ],
    [
      "2309",
      "3025"
    ],
    [
      "2320",
      "2289"
    ],
    [
      "2320",
      "2309"
    ],
    [
      "2320",
      "2420"
    ],
    [
      "2320",
      "2425"
    ],
    [
      "2397",
      "2399"
    ],
    [
      "2399",
      "2320"
    ],
    [
      "2399",
      "2420"
    ],
    [
      "2420",
      "2423"
    ],
    [
      "2423",
      "2420"
    ],
    [
      "2423",
      "2425"
    ],
    [
      "2425",
      "2437"
    ],
    [
      "2432",
      "2433"
    ],
    [
      "2433",
      "2263"
    ],
    [
      "2437",
      "2432"
    ],
    [
      "2467",
      "3230"
    ],
    [
      "2494",
      "3368"
    ],
    [
      "2498",
      "2494"
    ],
    [
      "2499",
      "2498"
    ],
    [
      "2535",
      "2882"
    ],
    [
      "2535",
      "2884"
    ],
    [
      "2552",
      "2864"
    ],
    [
      "2552",
      "424"
    ],
    [
      "2563",
      "2840"
    ],
    [
      "2563",
      "3125"
    ],
    [
      "2563",
      "3393"
    ],
    [
      "2692",
      "3393"
    ],
    [
      "2810",
      "3177"
    ],
    [
      "2823",
      "2840"
    ],
    [
      "2840",
      "2552"
    ],
    [
      "2840",
      "2863"
    ],
    [
      "2840",
      "424"
    ],
    [
      "2843",
      "2855"
    ],
    [
      "2843",
      "3177"
    ],
    [
      "2843",
      "3388"
    ],
    [
      "2855",
      "3275"
    ],
    [
      "2863",
      "2552"
    ],
    [
      "2864",
      "2855"
    ],
    [
      "2864",
      "3388"
    ],
    [
      "2882",
      "418"
    ],
    [
      "2884",
      "3275"
    ],
    [
      "2981",
      "3131"
    ],
    [
      "3000",
      "2552"
    ],
    [
      "3000",
      "2864"
    ],
    [
      "3000",
      "424"
    ],
    [
      "3025",
      "2218"
    ],
    [
      "3059",
      "3236"
    ],
    [
      "3077",
      "3059"
    ],
    [
      "3117",
      "3059"
    ],
    [
      "3117",
      "3240"
    ],
    [
      "3119",
      "3117"
    ],
    [
      "3125",
      "2563"
    ],
    [
      "3125",
      "2840"
    ],
    [
      "3131",
      "3167"
    ],
    [
      "3167",
      "3000"
    ],
    [
      "3177",
      "2855"
    ],
    [
      "3177",
      "3285"
    ],
    [
      "3177",
      "3388"
    ],
    [
      "3217",
      "3167"
    ],
    [
      "3230",
      "3289"
    ],
    [
      "3236",
      "3025"
    ],
    [
      "3236",
      "3217"
    ],
    [
      "3240",
      "3059"
    ],
    [
      "3246",
      "2467"
    ],
    [
      "3272",
      "2882"
    ],
    [
      "3272",
      "2884"
    ],
    [
      "3275",
      "2882"
    ],
    [
      "3275",
      "2884"
    ],
    [
      "3276",
      "3275"
    ],
    [
      "3285",
      "2855"
    ],
    [
      "3285",
      "3388"
    ],
    [
      "3289",
      "3246"
    ],
    [
      "3368",
      "3077"
    ],
    [
      "3381",
      "2535"
    ],
    [
      "3388",
      "3390"
    ],
    [
      "3390",
      "2535"
    ],
    [
      "3393",
      "2563"
    ],
    [
      "3393",
      "2840"
    ],
    [
      "415",
      "3059"
    ],
    [
      "415",
      "3240"
    ],
    [
      "418",
      "2884"
    ],
    [
      "424",
      "2864"
    ],
    [
      "449",
      "2882"
    ]
  ],
  "node_profiles": [
    {
      "node_id": "2012",
      "attributes": {
        "citycode": "torino",
        "detid": "2012",
        "fclass": "residential",
        "lanes": "3.0",
        "lat": "45.1161",
        "length": "0.422047308477787",
        "limit": "0",
        "linkid": "85.0",
        "long": "7.70912",
        "pos": "0.406484141887302",
        "road": "Corso Giulio Cesare"
      },
      "l2_labels": [
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "2218",
      "attributes": {
        "citycode": "torino",
        "detid": "2218",
        "fclass": "secondary",
        "lanes": "2.0",
        "lat": "45.0718659",
        "length": "0.289347869028938",
        "limit": "0",
        "linkid": "250.0",
        "long": "7.706338",
        "pos": "0.233261765866812",
        "road": "Corso Belgio"
      },
      "l2_labels": [
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:Residential",
        "FunctionalAreaType:WorkStudy"
      ]
    },
    {
      "node_id": "2222",
      "attributes": {
        "citycode": "torino",
        "detid": "2222",
        "fclass": "secondary",
        "lanes": "4.0",
        "lat": "45.0753057",
        "length": "0.067952878548871",
        "limit": "0",
        "linkid": "72.0",
        "long": "7.7047022",
        "pos": "0.036973539215549",
        "road": "Corso Novara"
      },
      "l2_labels": [
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:Residential",
        "FunctionalAreaType:WorkStudy"
      ]
    },
    {
      "node_id": "2256",
      "attributes": {
        "citycode": "torino",
        "detid": "2256",
        "fclass": "secondary",
        "lanes": "2.0",
        "lat": "45.0849227",
        "length": "0.258730805630355",
        "limit": "0",
        "linkid": "75.0",
        "long": "7.6960397",
        "pos": "0.250068407910821",
        "road": "Corso Novara"
      },
      "l2_labels": [
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:MedicalHealth",
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "2259",
      "attributes": {
        "citycode": "torino",
        "detid": "2259",
        "fclass": "secondary",
        "lanes": "2.0",
        "lat": "45.0867",
        "length": "0.254717010194845",
        "limit": "0",
        "linkid": "293.0",
        "long": "7.70496",
        "pos": "0.24302398837655",
        "road": "Via Bologna"
      },
      "l2_labels": [
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "2263",
      "attributes": {
        "citycode": "torino",
        "detid": "2263",
        "fclass": "secondary",
        "lanes": "2.0",
        "lat": "45.0794",
        "length": "0.188585942996422",
        "limit": "0",
        "linkid": "260.0",
        "long": "7.70075",
        "pos": "0.179032880456044",
        "road": "Corso Novara"
      },
      "l2_labels": [
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:CultureLeisure",
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "2289",
      "attributes": {
        "citycode": "torino",
        "detid": "2289",
        "fclass": "secondary",
        "lanes": "2.0",
        "lat": "45.0759218",
        "length": "0.053256660347761",
        "limit": "0",
        "linkid": "262.0",
        "long": "7.6920666",
        "pos": "0.041558801897949",
        "road": "Corso Regio Parco"
      },
      "l2_labels": [
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:CultureLeisure",
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "2309",
      "attributes": {
        "citycode": "torino",
        "detid": "2309",
        "fclass": "tertiary",
        "lanes": "1.0",
        "lat": "45.0807",
        "length": "0.206631546498928",
        "limit": "0",
        "linkid": "312.0",
        "long": "7.68618",
        "pos": "0.19336217907069",
        "road": "Corso Giulio Cesare"
      },
      "l2_labels": [
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:MedicalHealth",
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "2320",
      "attributes": {
        "citycode": "torino",
        "detid": "2320",
        "fclass": "tertiary",
        "lanes": "2.0",
        "lat": "45.0835",
        "length": "0.130426221266375",
        "limit": "0",
        "linkid": "310.0",
        "long": "7.686",
        "pos": "0.119501293728158",
        "road": "Corso Emilia"
      },
      "l2_labels": [
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "2397",
      "attributes": {
        "citycode": "torino",
        "detid": "2397",
        "fclass": "tertiary",
        "lanes": "2.0",
        "lat": "45.0971",
        "length": "0.257269895649133",
        "limit": "0",
        "linkid": "342.0",
        "long": "7.67146",
        "pos": "0.23573118291852",
        "road": "Via Stradella"
      },
      "l2_labels": [
        "FunctionalAreaType:AdministrativePublicService",
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "2399",
      "attributes": {
        "citycode": "torino",
        "detid": "2399",
        "fclass": "tertiary",
        "lanes": "2.0",
        "lat": "45.0963",
        "length": "0.264048796226683",
        "limit": "0",
        "linkid": "340.0",
        "long": "7.67222",
        "pos": "0.252207476644397",
        "road": "Via Stradella"
      },
      "l2_labels": [
        "FunctionalAreaType:AdministrativePublicService",
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "2420",
      "attributes": {
        "citycode": "torino",
        "detid": "2420",
        "fclass": "other",
        "lanes": "3.0",
        "lat": "45.0887",
        "length": "0.196300276961941",
        "limit": "0",
        "linkid": "299.0",
        "long": "7.6885",
        "pos": "0.190214093412663",
        "road": "Corso Novara"
      },
      "l2_labels": [
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:MedicalHealth",
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "2423",
      "attributes": {
        "citycode": "torino",
        "detid": "2423",
        "fclass": "secondary",
        "lanes": "2.0",
        "lat": "45.088",
        "length": "0.192803433064079",
        "limit": "0",
        "linkid": "300.0",
        "long": "7.69046",
        "pos": "0.177160271134232",
        "road": "Corso Novara"
      },
      "l2_labels": [
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:MedicalHealth",
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "2425",
      "attributes": {
        "citycode": "torino",
        "detid": "2425",
        "fclass": "secondary",
        "lanes": "2.0",
        "lat": "45.0876588",
        "length": "0.188917315241196",
        "limit": "0",
        "linkid": "101.0",
        "long": "7.6910531",
        "pos": "0.175869559711344",
        "road": "Corso Novara"
      },
      "l2_labels": [
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:MedicalHealth",
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "2432",
      "attributes": {
        "citycode": "torino",
        "detid": "2432",
        "fclass": "secondary",
        "lanes": "2.0",
        "lat": "45.0862",
        "length": "0.258044731602455",
        "limit": "0",
        "linkid": "76.0",
        "long": "7.69369",
        "pos": "0.242512742123235",
        "road": "Corso Novara"
      },
      "l2_labels": [
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:MedicalHealth",
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "2433",
      "attributes": {
        "citycode": "torino",
        "detid": "2433",
        "fclass": "secondary",
        "lanes": "2.0",
        "lat": "45.0847",
        "length": "0.179344056531085",
        "limit": "0",
        "linkid": "269.0",
        "long": "7.69613",
        "pos": "0.170388884366271",
        "road": "Corso Novara"
      },
      "l2_labels": [
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:MedicalHealth",
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "2437",
      "attributes": {
        "citycode": "torino",
        "detid": "2437",
        "fclass": "other",
        "lanes": "2.0",
        "lat": "45.0868473",
        "length": "0.18619150949042",
        "limit": "0",
        "linkid": "77.0",
        "long": "7.6927891",
        "pos": "0.177311330713539",
        "road": "Corso Novara"
      },
      "l2_labels": [
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:MedicalHealth",
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "2467",
      "attributes": {
        "citycode": "torino",
        "detid": "2467",
        "fclass": "primary",
        "lanes": "3.0",
        "lat": "45.1045",
        "length": "0.183785074607006",
        "limit": "0",
        "linkid": "83.0",
        "long": "7.70155",
        "pos": "0.174090761214594",
        "road": "Corso Giulio Cesare"
      },
      "l2_labels": [
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "2494",
      "attributes": {
        "citycode": "torino",
        "detid": "2494",
        "fclass": "primary",
        "lanes": "4.0",
        "lat": "45.1043546",
        "length": "0.162354028677839",
        "limit": "0",
        "linkid": "334.0",
        "long": "7.6811166",
        "pos": "0.145948970844898",
        "road": "Corso Grosseto"
      },
      "l2_labels": [
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "2498",
      "attributes": {
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
      "l2_labels": [
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "2499",
      "attributes": {
        "citycode": "torino",
        "detid": "2499",
        "fclass": "tertiary",
        "lanes": "2.0",
        "lat": "45.1044",
        "length": "0.130191985770544",
        "limit": "30",
        "linkid": "331.0",
        "long": "7.68489",
        "pos": "0.122902151636637",
        "road": "Via Ala di Stura"
      },
      "l2_labels": [
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "2535",
      "attributes": {
        "citycode": "torino",
        "detid": "2535",
        "fclass": "tertiary",
        "lanes": "2.0",
        "lat": "45.0457",
        "length": "0.126647081256806",
        "limit": "50",
        "linkid": "170.0",
        "long": "7.64497",
        "pos": "0.098185737136779",
        "road": "Corso Orbassano"
      },
      "l2_labels": [
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:MedicalHealth",
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "2552",
      "attributes": {
        "citycode": "torino",
        "detid": "2552",
        "fclass": "primary",
        "lanes": "3.0",
        "lat": "45.0326",
        "length": "0.189262109050561",
        "limit": "0",
        "linkid": "25.0",
        "long": "7.64665",
        "pos": "0.181113434671888",
        "road": "Corso Eusebio Giambone"
      },
      "l2_labels": [
        "FunctionalAreaType:AdministrativePublicService",
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "2563",
      "attributes": {
        "citycode": "torino",
        "detid": "2563",
        "fclass": "tertiary",
        "lanes": "3.0",
        "lat": "45.0221",
        "length": "0.15807088674997",
        "limit": "0",
        "linkid": "212.0",
        "long": "7.65069",
        "pos": "0.154125771548019",
        "road": "Via Pio VII"
      },
      "l2_labels": [
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:MedicalHealth",
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "2692",
      "attributes": {
        "citycode": "torino",
        "detid": "2692",
        "fclass": "secondary",
        "lanes": "3.0",
        "lat": "45.0178",
        "length": "0.07147126103329",
        "limit": "50",
        "linkid": "112.0",
        "long": "7.66176",
        "pos": "0.056149366680347",
        "road": "Via Nizza"
      },
      "l2_labels": [
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:Residential",
        "FunctionalAreaType:Transport"
      ]
    },
    {
      "node_id": "2810",
      "attributes": {
        "citycode": "torino",
        "detid": "2810",
        "fclass": "primary_link",
        "lanes": "4.0",
        "lat": "45.0316",
        "length": "0.117056799092012",
        "limit": "0",
        "linkid": "375.0",
        "long": "7.61537",
        "pos": "0.068027772331062",
        "road": "Corso Orbassano"
      },
      "l2_labels": []
    },
    {
      "node_id": "2823",
      "attributes": {
        "citycode": "torino",
        "detid": "2823",
        "fclass": "secondary",
        "lanes": "3.0",
        "lat": "45.0232981",
        "length": "0.145657247309153",
        "limit": "0",
        "linkid": "28.0",
        "long": "7.6352983",
        "pos": "0.141131983560511",
        "road": "Corso Giovanni Agnelli"
      },
      "l2_labels": [
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "2840",
      "attributes": {
        "citycode": "torino",
        "detid": "2840",
        "fclass": "secondary",
        "lanes": "3.0",
        "lat": "45.0307209",
        "length": "0.13490384541366",
        "limit": "0",
        "linkid": "194.0",
        "long": "7.6402861",
        "pos": "0.128968459112121",
        "road": "Corso Giovanni Agnelli"
      },
      "l2_labels": [
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "2843",
      "attributes": {
        "citycode": "torino",
        "detid": "2843",
        "fclass": "tertiary",
        "lanes": "2.0",
        "lat": "45.0346417",
        "length": "0.692294146394976",
        "limit": "0",
        "linkid": "368.0",
        "long": "7.6281041",
        "pos": "0.205121402431673",
        "road": "Corso Enrico Tazzoli"
      },
      "l2_labels": [
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "2855",
      "attributes": {
        "citycode": "torino",
        "detid": "2855",
        "fclass": "primary",
        "lanes": "3.0",
        "lat": "45.0409",
        "length": "0.221173830521114",
        "limit": "0",
        "linkid": "40.0",
        "long": "7.63407",
        "pos": "0.207099503848397",
        "road": "Corso Siracusa"
      },
      "l2_labels": [
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "2863",
      "attributes": {
        "citycode": "torino",
        "detid": "2863",
        "fclass": "primary",
        "lanes": "3.0",
        "lat": "45.035826",
        "length": "0.178374135574848",
        "limit": "50",
        "linkid": "197.0",
        "long": "7.6409877",
        "pos": "0.162417859034491",
        "road": "Corso Cosenza"
      },
      "l2_labels": [
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "2864",
      "attributes": {
        "citycode": "torino",
        "detid": "2864",
        "fclass": "primary",
        "lanes": "3.0",
        "lat": "45.0362848",
        "length": "0.140311532008665",
        "limit": "50",
        "linkid": "198.0",
        "long": "7.6406632",
        "pos": "0.130655077342903",
        "road": "Corso Cosenza"
      },
      "l2_labels": [
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "2882",
      "attributes": {
        "citycode": "torino",
        "detid": "2882",
        "fclass": "secondary",
        "lanes": "3.0",
        "lat": "45.0492773",
        "length": "0.143009596743216",
        "limit": "0",
        "linkid": "175.0",
        "long": "7.6336493",
        "pos": "0.130522197160485",
        "road": "Corso Sebastopoli"
      },
      "l2_labels": [
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "2884",
      "attributes": {
        "citycode": "torino",
        "detid": "2884",
        "fclass": "other",
        "lanes": "3.0",
        "lat": "45.0485",
        "length": "0.289156806396002",
        "limit": "0",
        "linkid": "47.0",
        "long": "7.63428",
        "pos": "0.263343163806309",
        "road": "Corso Siracusa"
      },
      "l2_labels": [
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "2981",
      "attributes": {
        "citycode": "torino",
        "detid": "2981",
        "fclass": "secondary",
        "lanes": "2.0",
        "lat": "45.0532",
        "length": "0.265007860212944",
        "limit": "0",
        "linkid": "13.0",
        "long": "7.6694",
        "pos": "0.260982296358989",
        "road": "Corso Filippo Turati"
      },
      "l2_labels": [
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:Residential",
        "FunctionalAreaType:Transport"
      ]
    },
    {
      "node_id": "3000",
      "attributes": {
        "citycode": "torino",
        "detid": "3000",
        "fclass": "other",
        "lanes": "2.0",
        "lat": "45.0377",
        "length": "0.183440018477611",
        "limit": "50",
        "linkid": "39.0",
        "long": "7.64494",
        "pos": "0.168542007913031",
        "road": "Corso Giovanni Agnelli"
      },
      "l2_labels": [
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "3025",
      "attributes": {
        "citycode": "torino",
        "detid": "3025",
        "fclass": "primary",
        "lanes": "2.0",
        "lat": "45.0717568",
        "length": "0.440566186419122",
        "limit": "0",
        "linkid": "68.0",
        "long": "7.6988435",
        "pos": "0.426684902862203",
        "road": "Corso Regina Margherita"
      },
      "l2_labels": [
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:CultureLeisure",
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "3059",
      "attributes": {
        "citycode": "torino",
        "detid": "3059",
        "fclass": "primary",
        "lanes": "2.0",
        "lat": "45.0847",
        "length": "0.457572018038187",
        "limit": "0",
        "linkid": "363.0",
        "long": "7.65944",
        "pos": "0.20785010792391",
        "road": "Corso Regina Margherita"
      },
      "l2_labels": [
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:MedicalHealth",
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "3077",
      "attributes": {
        "citycode": "torino",
        "detid": "3077",
        "fclass": "primary",
        "lanes": "3.0",
        "lat": "45.1003",
        "length": "0.181956600692776",
        "limit": "0",
        "linkid": "90.0",
        "long": "7.66007",
        "pos": "0.177598104970668",
        "road": "Corso Potenza"
      },
      "l2_labels": [
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "3117",
      "attributes": {
        "citycode": "torino",
        "detid": "3117",
        "fclass": "secondary",
        "lanes": "2.0",
        "lat": "45.0594",
        "length": "0.175547816192972",
        "limit": "0",
        "linkid": "94.0",
        "long": "7.66313",
        "pos": "0.163882056421329",
        "road": "Corso Luigi Einaudi"
      },
      "l2_labels": [
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "3119",
      "attributes": {
        "citycode": "torino",
        "detid": "3119",
        "fclass": "other",
        "lanes": "2.0",
        "lat": "45.0587",
        "length": "0.070228337418778",
        "limit": "0",
        "linkid": "110.0",
        "long": "7.66474",
        "pos": "0.050122811283619",
        "road": "Corso Luigi Einaudi"
      },
      "l2_labels": [
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "3125",
      "attributes": {
        "citycode": "torino",
        "detid": "3125",
        "fclass": "secondary",
        "lanes": "2.0",
        "lat": "45.0241209",
        "length": "0.157594153320959",
        "limit": "0",
        "linkid": "26.0",
        "long": "7.6367732",
        "pos": "0.13988825683468",
        "road": "Corso Unione Sovietica"
      },
      "l2_labels": [
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "3131",
      "attributes": {
        "citycode": "torino",
        "detid": "3131",
        "fclass": "tertiary",
        "lanes": "2.0",
        "lat": "45.0526",
        "length": "0.388609889158092",
        "limit": "0",
        "linkid": "104.0",
        "long": "7.65843",
        "pos": "0.159266874228126",
        "road": "Corso Carlo e Nello Rosselli"
      },
      "l2_labels": [
        "FunctionalAreaType:AdministrativePublicService",
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "3167",
      "attributes": {
        "citycode": "torino",
        "detid": "3167",
        "fclass": "secondary",
        "lanes": "4.0",
        "lat": "45.0526",
        "length": "0.11081596719809",
        "limit": "0",
        "linkid": "155.0",
        "long": "7.65556",
        "pos": "0.090772800772064",
        "road": "Largo Orbassano"
      },
      "l2_labels": [
        "FunctionalAreaType:AdministrativePublicService",
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "3177",
      "attributes": {
        "citycode": "torino",
        "detid": "3177",
        "fclass": "secondary",
        "lanes": "3.0",
        "lat": "45.0386",
        "length": "0.21594682408559",
        "limit": "0",
        "linkid": "367.0",
        "long": "7.62881",
        "pos": "0.198253325813328",
        "road": "Via Guido Reni"
      },
      "l2_labels": [
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "3217",
      "attributes": {
        "citycode": "torino",
        "detid": "3217",
        "fclass": "secondary",
        "lanes": "3.0",
        "lat": "45.0591773",
        "length": "0.180933780884157",
        "limit": "0",
        "linkid": "122.0",
        "long": "7.6562244",
        "pos": "0.164379500205306",
        "road": "Corso Mediterraneo"
      },
      "l2_labels": [
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:CultureLeisure",
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "3230",
      "attributes": {
        "citycode": "torino",
        "detid": "3230",
        "fclass": "secondary",
        "lanes": "2.0",
        "lat": "45.1019318",
        "length": "0.115274893795766",
        "limit": "0",
        "linkid": "281.0",
        "long": "7.7000266",
        "pos": "0.102047612202353",
        "road": "Corso Giulio Cesare"
      },
      "l2_labels": [
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:MedicalHealth",
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "3236",
      "attributes": {
        "citycode": "torino",
        "detid": "3236",
        "fclass": "primary",
        "lanes": "2.0",
        "lat": "45.083",
        "length": "0.170202631991675",
        "limit": "0",
        "linkid": "57.0",
        "long": "7.66461",
        "pos": "0.165662467129594",
        "road": "Corso Regina Margherita"
      },
      "l2_labels": [
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:MedicalHealth",
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "3240",
      "attributes": {
        "citycode": "torino",
        "detid": "3240",
        "fclass": "primary",
        "lanes": "3.0",
        "lat": "45.0727763",
        "length": "0.112208996609716",
        "limit": "0",
        "linkid": "133.0",
        "long": "7.641371",
        "pos": "0.102336487850673",
        "road": "Corso Trapani"
      },
      "l2_labels": [
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:Residential",
        "FunctionalAreaType:Transport"
      ]
    },
    {
      "node_id": "3246",
      "attributes": {
        "citycode": "torino",
        "detid": "3246",
        "fclass": "primary",
        "lanes": "3.0",
        "lat": "45.1089962",
        "length": "0.39119991642953",
        "limit": "0",
        "linkid": "84.0",
        "long": "7.7048602",
        "pos": "0.367663742858167",
        "road": "Corso Giulio Cesare"
      },
      "l2_labels": [
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "3272",
      "attributes": {
        "citycode": "torino",
        "detid": "3272",
        "fclass": "primary",
        "lanes": "4.0",
        "lat": "45.0506318",
        "length": "0.176172421683524",
        "limit": "0",
        "linkid": "49.0",
        "long": "7.6344745",
        "pos": "0.160670571330368",
        "road": "Corso Siracusa"
      },
      "l2_labels": [
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "3275",
      "attributes": {
        "citycode": "torino",
        "detid": "3275",
        "fclass": "primary",
        "lanes": "3.0",
        "lat": "45.0464455",
        "length": "0.286283950439297",
        "limit": "0",
        "linkid": "45.0",
        "long": "7.6343812",
        "pos": "0.249205282168827",
        "road": "Corso Siracusa"
      },
      "l2_labels": [
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "3276",
      "attributes": {
        "citycode": "torino",
        "detid": "3276",
        "fclass": "primary",
        "lanes": "3.0",
        "lat": "45.0453829",
        "length": "0.261010378458376",
        "limit": "0",
        "linkid": "46.0",
        "long": "7.6341563",
        "pos": "0.230289857646625",
        "road": "Corso Siracusa"
      },
      "l2_labels": [
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "3285",
      "attributes": {
        "citycode": "torino",
        "detid": "3285",
        "fclass": "residential",
        "lanes": "3.0",
        "lat": "45.0427",
        "length": "0.225002924528718",
        "limit": "0",
        "linkid": "41.0",
        "long": "7.63394",
        "pos": "0.207966425229859",
        "road": "Corso Siracusa"
      },
      "l2_labels": [
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "3289",
      "attributes": {
        "citycode": "torino",
        "detid": "3289",
        "fclass": "secondary",
        "lanes": "2.0",
        "lat": "45.0995",
        "length": "0.181289395169259",
        "limit": "0",
        "linkid": "81.0",
        "long": "7.69851",
        "pos": "0.170529864759649",
        "road": "Corso Giulio Cesare"
      },
      "l2_labels": [
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:MedicalHealth",
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "3368",
      "attributes": {
        "citycode": "torino",
        "detid": "3368",
        "fclass": "primary",
        "lanes": "2.0",
        "lat": "45.1012735",
        "length": "0.624593523210932",
        "limit": "0",
        "linkid": "91.0",
        "long": "7.660809",
        "pos": "0.096260648547929",
        "road": "Corso Potenza"
      },
      "l2_labels": [
        "FunctionalAreaType:AdministrativePublicService",
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "3381",
      "attributes": {
        "citycode": "torino",
        "detid": "3381",
        "fclass": "residential",
        "lanes": "2.0",
        "lat": "45.0493",
        "length": "0.362830024931042",
        "limit": "0",
        "linkid": "169.0",
        "long": "7.65057",
        "pos": "0.349525179025904",
        "road": "Via Caprera"
      },
      "l2_labels": [
        "FunctionalAreaType:AdministrativePublicService",
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "3388",
      "attributes": {
        "citycode": "torino",
        "detid": "3388",
        "fclass": "secondary",
        "lanes": "2.0",
        "lat": "45.041",
        "length": "0.115697992757818",
        "limit": "50",
        "linkid": "42.0",
        "long": "7.63568",
        "pos": "0.090518749916042",
        "road": "Corso Orbassano"
      },
      "l2_labels": [
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "3390",
      "attributes": {
        "citycode": "torino",
        "detid": "3390",
        "fclass": "secondary",
        "lanes": "2.0",
        "lat": "45.0419",
        "length": "0.187199800103915",
        "limit": "50",
        "linkid": "172.0",
        "long": "7.63786",
        "pos": "0.182022859066497",
        "road": "Corso Orbassano"
      },
      "l2_labels": [
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:MedicalHealth",
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "3393",
      "attributes": {
        "citycode": "torino",
        "detid": "3393",
        "fclass": "secondary",
        "lanes": "2.0",
        "lat": "45.0206",
        "length": "0.139685950522315",
        "limit": "0",
        "linkid": "214.0",
        "long": "7.65451",
        "pos": "0.131943119541882",
        "road": "Corso Traiano"
      },
      "l2_labels": [
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:MedicalHealth",
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "415",
      "attributes": {
        "citycode": "torino",
        "detid": "415",
        "fclass": "primary",
        "lanes": "3.0",
        "lat": "45.0888",
        "length": "0.371671431368054",
        "limit": "70",
        "linkid": "319.0",
        "long": "7.64708",
        "pos": "0.080373126337687",
        "road": "Corso Regina Margherita"
      },
      "l2_labels": [
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "418",
      "attributes": {
        "citycode": "torino",
        "detid": "418",
        "fclass": "secondary",
        "lanes": "2.0",
        "lat": "45.0494341",
        "length": "0.156411313202171",
        "limit": "0",
        "linkid": "48.0",
        "long": "7.6324361",
        "pos": "0.123746429313795",
        "road": "Corso Sebastopoli"
      },
      "l2_labels": [
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "424",
      "attributes": {
        "citycode": "torino",
        "detid": "424",
        "fclass": "secondary",
        "lanes": "3.0",
        "lat": "45.0338114",
        "length": "0.337118946599741",
        "limit": "0",
        "linkid": "36.0",
        "long": "7.6424017",
        "pos": "0.094295402767975",
        "road": "Corso Giovanni Agnelli"
      },
      "l2_labels": [
        "FunctionalAreaType:AdministrativePublicService",
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:Residential"
      ]
    },
    {
      "node_id": "449",
      "attributes": {
        "citycode": "torino",
        "detid": "449",
        "fclass": "secondary",
        "lanes": "3.0",
        "lat": "45.0222",
        "length": "0.315104227169236",
        "limit": "0",
        "linkid": "31.0",
        "long": "7.63488",
        "pos": "0.027734207604936",
        "road": "Corso Unione Sovietica"
      },
      "l2_labels": [
        "FunctionalAreaType:CommercialService",
        "FunctionalAreaType:Residential"
      ]
    }
  ],
  "selected_path": [
    "2498",
    "2494",
    "3368",
    "3077",
    "3059",
    "3236",
    "3217",
    "3167",
    "3000",
    "2864",
    "2855",
    "3275",
    "2882",
    "418"
  ]
}
```
