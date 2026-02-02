# V3AuditLogsAuditLogResponse

Represents an audit log entry response


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `id`                                                     | *int*                                                    | :heavy_check_mark:                                       | N/A                                                      |
| `resource`                                               | *str*                                                    | :heavy_check_mark:                                       | N/A                                                      |
| `action`                                                 | *str*                                                    | :heavy_check_mark:                                       | N/A                                                      |
| `actor`                                                  | [models.V3AuditLogsActor](../models/v3auditlogsactor.md) | :heavy_check_mark:                                       | Represents an actor (user) in audit logs                 |
| `client`                                                 | *str*                                                    | :heavy_check_mark:                                       | N/A                                                      |
| `timestamp`                                              | *str*                                                    | :heavy_check_mark:                                       | N/A                                                      |
| `team`                                                   | [models.V3AuditLogsTeam](../models/v3auditlogsteam.md)   | :heavy_check_mark:                                       | Represents a team in audit logs                          |