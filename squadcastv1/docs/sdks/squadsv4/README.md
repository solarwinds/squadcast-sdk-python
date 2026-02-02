# SquadsV4

## Overview

### Available Operations

* [create](#create) - Create Squad
* [update_name](#update_name) - Update Squad Name

## create

This endpoint is used to create a new squad.
The role will be considered only if your organization is on the OBAC permission model; otherwise, the role field will be ignored, and only the member will be added to the squad.

Requires `access_token` as a `Bearer {{token}}` in the `Authorization` header with `squad-create` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="Squads_createSquad" method="post" path="/v4/squads" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.squads_v4.create(owner_id="<id>", name="<value>", members=[
        {
            "user_id": "<id>",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `owner_id`                                                              | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `name`                                                                  | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `members`                                                               | List[[models.V4SquadsSquadMember](../../models/v4squadssquadmember.md)] | :heavy_check_mark:                                                      | N/A                                                                     |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.SquadsCreateSquadResponse](../../models/squadscreatesquadresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.CommonV4Error              | 400, 401, 402, 403, 404, 409, 422 | application/json                  |
| errors.CommonV4Error              | 500, 502, 503, 504                | application/json                  |
| errors.SDKDefaultError            | 4XX, 5XX                          | \*/\*                             |

## update_name

This endpoint is used to update squad's name.
Requires `access_token` as a `Bearer {{token}}` in the `Authorization` header with `squad-create` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="Squads_updateSquadName" method="put" path="/v4/squads/{squadID}/name" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.squads_v4.update_name(squad_id="<id>", name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `squad_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SquadsUpdateSquadNameResponse](../../models/squadsupdatesquadnameresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.CommonV4Error              | 400, 401, 402, 403, 404, 409, 422 | application/json                  |
| errors.CommonV4Error              | 500, 502, 503, 504                | application/json                  |
| errors.SDKDefaultError            | 4XX, 5XX                          | \*/\*                             |