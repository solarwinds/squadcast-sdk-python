# V3IncidentsTagsNotificationDelayPolicy

Policy for delaying notifications.


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `is_notification_delayed`                                              | *bool*                                                                 | :heavy_check_mark:                                                     | N/A                                                                    |
| `delayed_until`                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects)   | :heavy_check_mark:                                                     | N/A                                                                    |
| `assign_to`                                                            | [models.V3IncidentsTagsAssignTo](../models/v3incidentstagsassignto.md) | :heavy_check_mark:                                                     | Represents the assignment target for delayed notifications.            |