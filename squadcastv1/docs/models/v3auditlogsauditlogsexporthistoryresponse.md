# V3AuditLogsAuditLogsExportHistoryResponse

Response model for audit logs export history


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `id`                                                         | *str*                                                        | :heavy_check_mark:                                           | N/A                                                          |
| `name`                                                       | *str*                                                        | :heavy_check_mark:                                           | N/A                                                          |
| `description`                                                | *str*                                                        | :heavy_check_mark:                                           | N/A                                                          |
| `exported_at`                                                | *str*                                                        | :heavy_check_mark:                                           | N/A                                                          |
| `requested_by`                                               | [models.V3AuditLogsActor](../models/v3auditlogsactor.md)     | :heavy_check_mark:                                           | Represents an actor (user) in audit logs                     |
| `download_link`                                              | *str*                                                        | :heavy_check_mark:                                           | N/A                                                          |
| `status`                                                     | *str*                                                        | :heavy_check_mark:                                           | N/A                                                          |
| `filters`                                                    | [models.V3AuditLogsFilters](../models/v3auditlogsfilters.md) | :heavy_check_mark:                                           | Represents filters used in audit log queries                 |