# V3TeamsAddBulkTeamMemberRequestMember


## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `user_id`                                                     | *str*                                                         | :heavy_check_mark:                                            | N/A                                                           |
| `role`                                                        | *Optional[str]*                                               | :heavy_minus_sign:                                            | this field is required if you are using OBAC permission model |
| `role_ids`                                                    | List[*str*]                                                   | :heavy_check_mark:                                            | this field is required if you are using RBAC permission model |