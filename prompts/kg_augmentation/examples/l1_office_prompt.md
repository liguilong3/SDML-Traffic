# l1_office: complete presentation example

## Instructions

Use only the supplied evidence and fixed output schema. Distinguish provided facts from semantic interpretations. Return supported values with evidence references and concise rationales. Abstain when evidence is insufficient. Do not use traffic states, occupancy histories, downstream results, or invented connections. Accepted judgments require human review before integration.

For each supplied native POI type, select one supported Function value or ABSTAIN. Use the native type as the primary evidence and apply the accepted mapping consistently to corresponding POIs. Return scene, native_type, function, and rationale.

## Allowed relations and values

```json
{
  "has_functional_category": {
    "level": "L1",
    "head_type": "POI",
    "tail_type": "Function",
    "allowed_values": [
      "Function:Residential",
      "Function:WorkStudy",
      "Function:IndustrialLogistics",
      "Function:CommercialService",
      "Function:MedicalHealth",
      "Function:CultureLeisure",
      "Function:Transport",
      "Function:PublicService",
      "Function:VehicleSupport",
      "Function:Accommodation"
    ],
    "max_values_per_head": 3,
    "meaning": "Functional category inferred from the native POI type and assigned to that POI."
  }
}
```

## Concrete input

```json
{
  "scene": "flow",
  "level": "L1",
  "output_schema": {
    "has_functional_category": {
      "level": "L1",
      "head_type": "POI",
      "tail_type": "Function",
      "allowed_values": [
        "Function:Residential",
        "Function:WorkStudy",
        "Function:IndustrialLogistics",
        "Function:CommercialService",
        "Function:MedicalHealth",
        "Function:CultureLeisure",
        "Function:Transport",
        "Function:PublicService",
        "Function:VehicleSupport",
        "Function:Accommodation"
      ],
      "max_values_per_head": 3,
      "meaning": "Functional category inferred from the native POI type and assigned to that POI."
    }
  },
  "native_types": [
    "office"
  ]
}
```
