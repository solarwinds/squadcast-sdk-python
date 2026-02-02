# V3RunbooksUpdateRunbookRequest

Represents the request body for updating a runbook.


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `name`                                                                   | *str*                                                                    | :heavy_check_mark:                                                       | The name of the runbook.                                                 |
| `steps`                                                                  | List[[models.V3RunbooksStep](../models/v3runbooksstep.md)]               | :heavy_check_mark:                                                       | The steps that make up the runbook.                                      |
| `entity_owner`                                                           | [Optional[models.CommonV3EntityOwner]](../models/commonv3entityowner.md) | :heavy_minus_sign:                                                       | The owner of the entity.                                                 |