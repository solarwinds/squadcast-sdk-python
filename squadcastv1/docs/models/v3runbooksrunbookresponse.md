# V3RunbooksRunbookResponse

Represents a Runbook in the system.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | The unique identifier for the runbook.                               |
| `name`                                                               | *str*                                                                | :heavy_check_mark:                                                   | The name of the runbook.                                             |
| `created`                                                            | [models.V3RunbooksUpdationInfo](../models/v3runbooksupdationinfo.md) | :heavy_check_mark:                                                   | Information about when the runbook was created.                      |
| `updated`                                                            | [models.V3RunbooksUpdationInfo](../models/v3runbooksupdationinfo.md) | :heavy_check_mark:                                                   | Information about when the runbook was last updated.                 |
| `used_count`                                                         | *int*                                                                | :heavy_check_mark:                                                   | The number of times this runbook has been used.                      |
| `steps`                                                              | List[[models.V3RunbooksStep](../models/v3runbooksstep.md)]           | :heavy_check_mark:                                                   | The steps that make up the runbook.                                  |
| `entity_owner`                                                       | [models.CommonV3EntityOwner](../models/commonv3entityowner.md)       | :heavy_check_mark:                                                   | The owner of the entity.                                             |
| `organization_id`                                                    | *str*                                                                | :heavy_check_mark:                                                   | The ID of the organization this runbook belongs to.                  |
| `owner`                                                              | [models.CommonV3RBACOwner](../models/commonv3rbacowner.md)           | :heavy_check_mark:                                                   | The RBAC owner of the runbook (typically a team).                    |