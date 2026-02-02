# SchedulesListSchedulesRequest


## Fields

| Field                       | Type                        | Required                    | Description                 |
| --------------------------- | --------------------------- | --------------------------- | --------------------------- |
| `team_id`                   | *str*                       | :heavy_check_mark:          | N/A                         |
| `schedule_i_ds`             | List[*int*]                 | :heavy_minus_sign:          | N/A                         |
| `participants`              | List[*str*]                 | :heavy_minus_sign:          | N/A                         |
| `schedule_name`             | *Optional[str]*             | :heavy_minus_sign:          | N/A                         |
| `my_on_call`                | *Optional[bool]*            | :heavy_minus_sign:          | N/A                         |
| `you_and_your_squads`       | *Optional[bool]*            | :heavy_minus_sign:          | N/A                         |
| `search`                    | *Optional[str]*             | :heavy_minus_sign:          | N/A                         |
| `hide_paused`               | *Optional[bool]*            | :heavy_minus_sign:          | N/A                         |
| `owner_id`                  | *Optional[str]*             | :heavy_minus_sign:          | N/A                         |
| `escalation_policies`       | List[*str*]                 | :heavy_minus_sign:          | N/A                         |
| `without_escalation_policy` | *Optional[bool]*            | :heavy_minus_sign:          | N/A                         |
| `page_size`                 | *Optional[int]*             | :heavy_minus_sign:          | N/A                         |
| `cursor`                    | *Optional[str]*             | :heavy_minus_sign:          | N/A                         |