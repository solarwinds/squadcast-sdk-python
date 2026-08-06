# V3IncidentsMergeIntoExistingParentRequest

Request body for merging incidents into an existing parent incident.


## Fields

| Field                | Type                 | Required             | Description          |
| -------------------- | -------------------- | -------------------- | -------------------- |
| `owner_id`           | *str*                | :heavy_check_mark:   | N/A                  |
| `parent_incident_id` | *str*                | :heavy_check_mark:   | N/A                  |
| `children`           | List[*str*]          | :heavy_check_mark:   | N/A                  |