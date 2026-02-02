# V3AuditLogsFilters

Represents filters used in audit log queries


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `start_date`                                                                 | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects) | :heavy_check_mark:                                                           | N/A                                                                          |
| `end_date`                                                                   | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects) | :heavy_check_mark:                                                           | N/A                                                                          |
| `resource`                                                                   | List[*str*]                                                                  | :heavy_minus_sign:                                                           | N/A                                                                          |
| `action`                                                                     | List[*str*]                                                                  | :heavy_minus_sign:                                                           | N/A                                                                          |
| `actor`                                                                      | List[[models.V3AuditLogsActor](../models/v3auditlogsactor.md)]               | :heavy_minus_sign:                                                           | N/A                                                                          |
| `team`                                                                       | List[[models.V3AuditLogsTeam](../models/v3auditlogsteam.md)]                 | :heavy_minus_sign:                                                           | N/A                                                                          |
| `client`                                                                     | List[*str*]                                                                  | :heavy_minus_sign:                                                           | N/A                                                                          |