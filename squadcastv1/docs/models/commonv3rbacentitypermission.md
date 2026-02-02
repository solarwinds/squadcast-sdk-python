# CommonV3RBACEntityPermission

Represents a permission granted to a user for a specific entity.


## Fields

| Field                                        | Type                                         | Required                                     | Description                                  |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `user_id`                                    | *str*                                        | :heavy_check_mark:                           | The ID of the user receiving the permission. |
| `abilities`                                  | [models.Abilities](../models/abilities.md)   | :heavy_check_mark:                           | A map of abilities granted to the user.      |