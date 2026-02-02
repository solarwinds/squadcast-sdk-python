# Squads.Members

## Overview

### Available Operations

* [update](#update) - Update Squad Member

## update

This endpoint is used to update a squad member's role and is only accessible if your organization is using the OBAC permission model.

If you're attempting to update a member's role from 'owner' to 'member', and that 'owner' is the last squad owner, then the 'replaceWith' query parameter is required. Setting 'replaceWith' to 'member' will promote the member to the role of owner.

Requires `access_token` as a `Bearer {{token}}` in the `Authorization` header with `squad-create` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="Squads_updateSquadMember" method="put" path="/v4/squads/{squadID}/members/{memberID}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.squads.members.update(squad_id="<id>", member_id="<id>", replace_with="<value>", role="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `squad_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `member_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `replace_with`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `role`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.V4SquadsUpdateSquadMemberResponse](../../models/v4squadsupdatesquadmemberresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.CommonV4Error              | 400, 401, 402, 403, 404, 409, 422 | application/json                  |
| errors.CommonV4Error              | 500, 502, 503, 504                | application/json                  |
| errors.SDKDefaultError            | 4XX, 5XX                          | \*/\*                             |