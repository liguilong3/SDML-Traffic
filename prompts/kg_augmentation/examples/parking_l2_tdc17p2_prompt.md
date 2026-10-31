# parking_l2_tdc17p2: complete presentation example

## Instructions

Use only the supplied evidence and fixed output schema. Distinguish provided facts from semantic interpretations. Return supported values with evidence references and concise rationales. Abstain when evidence is insufficient. Do not use traffic states, occupancy histories, downstream results, or invented connections. Accepted judgments require human review before integration.

Using the facility name, supplied source attributes, and directly associated POI semantics, judge potential user group, use orientation, time-of-day orientation, and turnover tendency independently. Return at most one value per dimension, with supporting native types, attribute references, a rationale, or an abstention reason. Opening hours do not establish demand periods.

## Allowed relations and values

```json
{
  "has_potential_user_group": {
    "level": "L2",
    "head_type": "Parking",
    "tail_type": "UserGroup",
    "allowed_values": [
      "UserGroup:Visitors",
      "UserGroup:WorkStudyUsers",
      "UserGroup:Residents",
      "UserGroup:MixedUsers"
    ],
    "max_values_per_head": 1,
    "meaning": "A potential contextual prior, assessed independently from the other Parking L2 dimensions."
  },
  "has_use_orientation": {
    "level": "L2",
    "head_type": "Parking",
    "tail_type": "ParkingUse",
    "allowed_values": [
      "ParkingUse:VisitOriented",
      "ParkingUse:CommuteOriented",
      "ParkingUse:StayOriented",
      "ParkingUse:MixedUse"
    ],
    "max_values_per_head": 1,
    "meaning": "A potential contextual prior, assessed independently from the other Parking L2 dimensions."
  },
  "has_time_of_day_orientation": {
    "level": "L2",
    "head_type": "Parking",
    "tail_type": "ParkingPeriod",
    "allowed_values": [
      "ParkingPeriod:DaytimeOriented",
      "ParkingPeriod:NighttimeOriented",
      "ParkingPeriod:MixedPeriod"
    ],
    "max_values_per_head": 1,
    "meaning": "A potential contextual prior, assessed independently from the other Parking L2 dimensions."
  },
  "has_turnover_tendency": {
    "level": "L2",
    "head_type": "Parking",
    "tail_type": "TurnoverTendency",
    "allowed_values": [
      "TurnoverTendency:RelativelyFast",
      "TurnoverTendency:RelativelySlow",
      "TurnoverTendency:Mixed"
    ],
    "max_values_per_head": 1,
    "meaning": "A potential contextual prior, assessed independently from the other Parking L2 dimensions."
  }
}
```

## Concrete input

```json
{
  "scene": "parking",
  "level": "L2",
  "output_schema": {
    "has_potential_user_group": {
      "level": "L2",
      "head_type": "Parking",
      "tail_type": "UserGroup",
      "allowed_values": [
        "UserGroup:Visitors",
        "UserGroup:WorkStudyUsers",
        "UserGroup:Residents",
        "UserGroup:MixedUsers"
      ],
      "max_values_per_head": 1,
      "meaning": "A potential contextual prior, assessed independently from the other Parking L2 dimensions."
    },
    "has_use_orientation": {
      "level": "L2",
      "head_type": "Parking",
      "tail_type": "ParkingUse",
      "allowed_values": [
        "ParkingUse:VisitOriented",
        "ParkingUse:CommuteOriented",
        "ParkingUse:StayOriented",
        "ParkingUse:MixedUse"
      ],
      "max_values_per_head": 1,
      "meaning": "A potential contextual prior, assessed independently from the other Parking L2 dimensions."
    },
    "has_time_of_day_orientation": {
      "level": "L2",
      "head_type": "Parking",
      "tail_type": "ParkingPeriod",
      "allowed_values": [
        "ParkingPeriod:DaytimeOriented",
        "ParkingPeriod:NighttimeOriented",
        "ParkingPeriod:MixedPeriod"
      ],
      "max_values_per_head": 1,
      "meaning": "A potential contextual prior, assessed independently from the other Parking L2 dimensions."
    },
    "has_turnover_tendency": {
      "level": "L2",
      "head_type": "Parking",
      "tail_type": "TurnoverTendency",
      "allowed_values": [
        "TurnoverTendency:RelativelyFast",
        "TurnoverTendency:RelativelySlow",
        "TurnoverTendency:Mixed"
      ],
      "max_values_per_head": 1,
      "meaning": "A potential contextual prior, assessed independently from the other Parking L2 dimensions."
    }
  },
  "target_id": "tdc17p2",
  "target_attributes": {
    "displayAddress_en": "West Kowloon Cultural District, No.36 Museum Drive, Kowloon, Hong Kong",
    "displayAddress_sc": "香港九龙西九文化区博物馆路36号",
    "displayAddress_tc": "香港九龍西九文化區博物館路36號",
    "district_en": "Yau Tsim Mong",
    "district_sc": "油尖旺区",
    "district_tc": "油尖旺區",
    "height": "2.1",
    "latitude": "22.301193835199",
    "longitude": "114.15779746439",
    "name_en": "Art Park Car Park",
    "name_sc": "艺术公园停车场",
    "name_tc": "藝術公園停車場",
    "opening_status": "OPEN",
    "park_id": "tdc17p2",
    "remark_en": "Height Limit: Height limit:2.1(M)\nHourly Parking<br>Monday to Friday (Except Public Holidays) : $28/hr<br>\nSaturday, Sunday and Public Holidays : $32/hr<br><br>\nNight Park<br>Monday to Thursday (Except Public Holidays) : $80 per session (7:00pm-7:00am) <br>\nFriday to Sunday and Public Holidays : $100 per session (7:00pm-7:00am)<br><br>24 hours",
    "remark_sc": "高度限制: 高度限制2.1米\n时租<br>星期一至五 （公众假期除外）: 每小时$28<br>\n星期六丶日及公众假期 : 每小时$32<br><br>\n夜泊 <br>星期一至四 （公众假期除外）: 每节$80（晚上7时至上午7时） <br>\n星期五至日及公众假期 :每节$100（晚上7时至上午7时）<br><br>24小时",
    "remark_tc": "高度限制: 高度限制2.1米\n時租<br>星期一至五 （公眾假期除外）: 每小時$28<br>\n星期六、日及公眾假期 : 每小時$32<br><br>\n夜泊 <br>星期一至四 （公眾假期除外）: 每節$80（晚上7時至上午7時） <br>\n星期五至日及公眾假期 :每節$100（晚上7時至上午7時）<br><br>24小時",
    "website_en": "http://www.wkcda.hk/",
    "website_sc": "http://www.wkcda.hk/",
    "website_tc": "http://www.wkcda.hk/"
  },
  "direct_pois": [
    {
      "poi_id": "poi_node_10591704495",
      "native_types": [
        "OSM_POI_Type:stop_position"
      ],
      "functions": [
        "Function:Transport"
      ],
      "association_fact": [
        "tdc17p2",
        "nearby_poi",
        "poi_node_10591704495"
      ]
    },
    {
      "poi_id": "poi_node_10591704498",
      "native_types": [
        "OSM_POI_Type:taxi"
      ],
      "functions": [
        "Function:Transport"
      ],
      "association_fact": [
        "tdc17p2",
        "nearby_poi",
        "poi_node_10591704498"
      ]
    },
    {
      "poi_id": "poi_node_10591704499",
      "native_types": [
        "OSM_POI_Type:platform"
      ],
      "functions": [
        "Function:Transport"
      ],
      "association_fact": [
        "tdc17p2",
        "nearby_poi",
        "poi_node_10591704499"
      ]
    },
    {
      "poi_id": "poi_node_11276779937",
      "native_types": [
        "OSM_POI_Type:platform"
      ],
      "functions": [
        "Function:Transport"
      ],
      "association_fact": [
        "tdc17p2",
        "nearby_poi",
        "poi_node_11276779937"
      ]
    },
    {
      "poi_id": "poi_node_11730844148",
      "native_types": [
        "OSM_POI_Type:stop_position"
      ],
      "functions": [
        "Function:Transport"
      ],
      "association_fact": [
        "tdc17p2",
        "nearby_poi",
        "poi_node_11730844148"
      ]
    },
    {
      "poi_id": "poi_node_12086938543",
      "native_types": [
        "OSM_POI_Type:restaurant"
      ],
      "functions": [
        "Function:CommercialService"
      ],
      "association_fact": [
        "tdc17p2",
        "nearby_poi",
        "poi_node_12086938543"
      ]
    },
    {
      "poi_id": "poi_node_12511892645",
      "native_types": [
        "OSM_POI_Type:stop_position"
      ],
      "functions": [
        "Function:Transport"
      ],
      "association_fact": [
        "tdc17p2",
        "nearby_poi",
        "poi_node_12511892645"
      ]
    },
    {
      "poi_id": "poi_node_12968956235",
      "native_types": [
        "OSM_POI_Type:stop_position"
      ],
      "functions": [
        "Function:Transport"
      ],
      "association_fact": [
        "tdc17p2",
        "nearby_poi",
        "poi_node_12968956235"
      ]
    },
    {
      "poi_id": "poi_node_12968956237",
      "native_types": [
        "OSM_POI_Type:stop_position"
      ],
      "functions": [
        "Function:Transport"
      ],
      "association_fact": [
        "tdc17p2",
        "nearby_poi",
        "poi_node_12968956237"
      ]
    },
    {
      "poi_id": "poi_node_9810960029",
      "native_types": [
        "OSM_POI_Type:restaurant"
      ],
      "functions": [
        "Function:CommercialService"
      ],
      "association_fact": [
        "tdc17p2",
        "nearby_poi",
        "poi_node_9810960029"
      ]
    },
    {
      "poi_id": "poi_node_9978884006",
      "native_types": [
        "OSM_POI_Type:platform"
      ],
      "functions": [
        "Function:Transport"
      ],
      "association_fact": [
        "tdc17p2",
        "nearby_poi",
        "poi_node_9978884006"
      ]
    },
    {
      "poi_id": "poi_node_9978884007",
      "native_types": [
        "OSM_POI_Type:platform"
      ],
      "functions": [
        "Function:Transport"
      ],
      "association_fact": [
        "tdc17p2",
        "nearby_poi",
        "poi_node_9978884007"
      ]
    },
    {
      "poi_id": "poi_node_9978884008",
      "native_types": [
        "OSM_POI_Type:platform"
      ],
      "functions": [
        "Function:Transport"
      ],
      "association_fact": [
        "tdc17p2",
        "nearby_poi",
        "poi_node_9978884008"
      ]
    },
    {
      "poi_id": "poi_node_9978884009",
      "native_types": [
        "OSM_POI_Type:platform"
      ],
      "functions": [
        "Function:Transport"
      ],
      "association_fact": [
        "tdc17p2",
        "nearby_poi",
        "poi_node_9978884009"
      ]
    },
    {
      "poi_id": "poi_way_1068799340",
      "native_types": [
        "OSM_POI_Type:restaurant"
      ],
      "functions": [
        "Function:CommercialService"
      ],
      "association_fact": [
        "tdc17p2",
        "nearby_poi",
        "poi_way_1068799340"
      ]
    },
    {
      "poi_id": "poi_way_1068799341",
      "native_types": [
        "OSM_POI_Type:cinema"
      ],
      "functions": [
        "Function:CultureLeisure"
      ],
      "association_fact": [
        "tdc17p2",
        "nearby_poi",
        "poi_way_1068799341"
      ]
    },
    {
      "poi_id": "poi_way_1068799342",
      "native_types": [
        "OSM_POI_Type:cafe"
      ],
      "functions": [
        "Function:CommercialService"
      ],
      "association_fact": [
        "tdc17p2",
        "nearby_poi",
        "poi_way_1068799342"
      ]
    },
    {
      "poi_id": "poi_way_1068799343",
      "native_types": [
        "OSM_POI_Type:gift"
      ],
      "functions": [
        "Function:CommercialService"
      ],
      "association_fact": [
        "tdc17p2",
        "nearby_poi",
        "poi_way_1068799343"
      ]
    },
    {
      "poi_id": "poi_way_1068799347",
      "native_types": [
        "OSM_POI_Type:parking"
      ],
      "functions": [
        "Function:VehicleSupport"
      ],
      "association_fact": [
        "tdc17p2",
        "nearby_poi",
        "poi_way_1068799347"
      ]
    },
    {
      "poi_id": "poi_way_1068799348",
      "native_types": [
        "OSM_POI_Type:parking"
      ],
      "functions": [
        "Function:VehicleSupport"
      ],
      "association_fact": [
        "tdc17p2",
        "nearby_poi",
        "poi_way_1068799348"
      ]
    },
    {
      "poi_id": "poi_way_185036075",
      "native_types": [
        "OSM_POI_Type:office"
      ],
      "functions": [
        "Function:WorkStudy"
      ],
      "association_fact": [
        "tdc17p2",
        "nearby_poi",
        "poi_way_185036075"
      ]
    },
    {
      "poi_id": "poi_way_549702815",
      "native_types": [
        "OSM_POI_Type:building"
      ],
      "functions": [],
      "association_fact": [
        "tdc17p2",
        "nearby_poi",
        "poi_way_549702815"
      ]
    },
    {
      "poi_id": "poi_way_567801791",
      "native_types": [
        "OSM_POI_Type:park"
      ],
      "functions": [
        "Function:CultureLeisure"
      ],
      "association_fact": [
        "tdc17p2",
        "nearby_poi",
        "poi_way_567801791"
      ]
    },
    {
      "poi_id": "poi_way_791242998",
      "native_types": [
        "OSM_POI_Type:office"
      ],
      "functions": [
        "Function:WorkStudy"
      ],
      "association_fact": [
        "tdc17p2",
        "nearby_poi",
        "poi_way_791242998"
      ]
    },
    {
      "poi_id": "poi_way_984424587",
      "native_types": [
        "OSM_POI_Type:office"
      ],
      "functions": [
        "Function:WorkStudy"
      ],
      "association_fact": [
        "tdc17p2",
        "nearby_poi",
        "poi_way_984424587"
      ]
    }
  ]
}
```
