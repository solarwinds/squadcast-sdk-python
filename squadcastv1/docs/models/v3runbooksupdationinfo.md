# V3RunbooksUpdationInfo

Represents information about the creation or updation of an entity.


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `user_name`                                                              | *str*                                                                    | :heavy_check_mark:                                                       | The full name of the user who performed the action.                      |
| `username_for_display`                                                   | *str*                                                                    | :heavy_check_mark:                                                       | The display name of the user who performed the action.                   |
| `user_id`                                                                | *str*                                                                    | :heavy_check_mark:                                                       | The ID of the user who performed the action.                             |
| `at`                                                                     | [date](https://docs.python.org/3/library/datetime.html#date-objects)     | :heavy_check_mark:                                                       | The timestamp of the action.                                             |
| `entity_owner`                                                           | [Optional[models.CommonV3EntityOwner]](../models/commonv3entityowner.md) | :heavy_minus_sign:                                                       | The owner of the entity at the time of the action.                       |