# V3IncidentsNotesNoteResponse

Represents a note associated with an incident.


## Fields

| Field                            | Type                             | Required                         | Description                      |
| -------------------------------- | -------------------------------- | -------------------------------- | -------------------------------- |
| `id`                             | *str*                            | :heavy_check_mark:               | N/A                              |
| `created_at`                     | *str*                            | :heavy_check_mark:               | N/A                              |
| `updated_at`                     | *str*                            | :heavy_check_mark:               | N/A                              |
| `organization_id`                | *str*                            | :heavy_check_mark:               | N/A                              |
| `incident_id`                    | *str*                            | :heavy_check_mark:               | N/A                              |
| `user_id`                        | *str*                            | :heavy_check_mark:               | N/A                              |
| `message`                        | *str*                            | :heavy_check_mark:               | N/A                              |
| `type`                           | *str*                            | :heavy_check_mark:               | N/A                              |
| `attachments`                    | List[*str*]                      | :heavy_check_mark:               | N/A                              |
| `user`                           | [models.User](../models/user.md) | :heavy_check_mark:               | N/A                              |
| `replaced_message`               | *str*                            | :heavy_check_mark:               | N/A                              |