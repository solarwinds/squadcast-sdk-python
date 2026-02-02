# Postmortems

## Overview

### Available Operations

* [get_all](#get_all) - Get All Postmortems
* [create](#create) - Create Postmortem

## get_all

*   This endpoint is used to get all postmortems.
*   Requires `access_token` as a `Bearer {{token}}` in the `Authorization` header.

### Example Usage

<!-- UsageSnippet language="python" operationID="Postmortems_getAllPostmortems" method="get" path="/v3/incidents/postmortem" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.postmortems.get_all(from_date="<value>", to_date="<value>", owner_id="<id>", limit=221553)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `from_date`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Provide date in RFC3339 format                                      |
| `to_date`                                                           | *str*                                                               | :heavy_check_mark:                                                  | Provide date in RFC3339 format                                      |
| `owner_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Here owner_id represents team_id                                    |
| `limit`                                                             | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PostmortemsGetAllPostmortemsResponse](../../models/postmortemsgetallpostmortemsresponse.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.BadRequestError          | 400                             | application/json                |
| errors.UnauthorizedError        | 401                             | application/json                |
| errors.PaymentRequiredError     | 402                             | application/json                |
| errors.ForbiddenError           | 403                             | application/json                |
| errors.NotFoundError            | 404                             | application/json                |
| errors.ConflictError            | 409                             | application/json                |
| errors.UnprocessableEntityError | 422                             | application/json                |
| errors.InternalServerError      | 500                             | application/json                |
| errors.BadGatewayError          | 502                             | application/json                |
| errors.ServiceUnavailableError  | 503                             | application/json                |
| errors.GatewayTimeoutError      | 504                             | application/json                |
| errors.SDKDefaultError          | 4XX, 5XX                        | \*/\*                           |

## create

*   This endpoint is used to create a postmortem.
*   Requires `access_token` as a `Bearer {{token}}` in the `Authorization` header.

### Example Usage

<!-- UsageSnippet language="python" operationID="Postmortems_createPostmortem" method="post" path="/v3/incidents/{incidentID}/postmortem" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.postmortems.create(incident_id="<id>", owner_id="<id>", title="<value>", postmortem="<value>", status="published", follow_ups=[], attachments=[
        {},
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                           | Type                                                                                                                                | Required                                                                                                                            | Description                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `incident_id`                                                                                                                       | *str*                                                                                                                               | :heavy_check_mark:                                                                                                                  | N/A                                                                                                                                 |
| `owner_id`                                                                                                                          | *str*                                                                                                                               | :heavy_check_mark:                                                                                                                  | N/A                                                                                                                                 |
| `title`                                                                                                                             | *str*                                                                                                                               | :heavy_check_mark:                                                                                                                  | N/A                                                                                                                                 |
| `postmortem`                                                                                                                        | *str*                                                                                                                               | :heavy_check_mark:                                                                                                                  | N/A                                                                                                                                 |
| `status`                                                                                                                            | [models.V3IncidentsPostmortemsPostmortemStatus](../../models/v3incidentspostmortemspostmortemstatus.md)                             | :heavy_check_mark:                                                                                                                  | Represents the status of a postmortem.                                                                                              |
| `follow_ups`                                                                                                                        | List[[models.V3IncidentsPostmortemsPostmortemFollowUp](../../models/v3incidentspostmortemspostmortemfollowup.md)]                   | :heavy_check_mark:                                                                                                                  | N/A                                                                                                                                 |
| `attachments`                                                                                                                       | List[[models.V3IncidentsPostmortemsPostmortemAttachmentRequest](../../models/v3incidentspostmortemspostmortemattachmentrequest.md)] | :heavy_check_mark:                                                                                                                  | N/A                                                                                                                                 |
| `retries`                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                    | :heavy_minus_sign:                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                 |

### Response

**[models.PostmortemsCreatePostmortemResponse](../../models/postmortemscreatepostmortemresponse.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.BadRequestError          | 400                             | application/json                |
| errors.UnauthorizedError        | 401                             | application/json                |
| errors.PaymentRequiredError     | 402                             | application/json                |
| errors.ForbiddenError           | 403                             | application/json                |
| errors.NotFoundError            | 404                             | application/json                |
| errors.ConflictError            | 409                             | application/json                |
| errors.UnprocessableEntityError | 422                             | application/json                |
| errors.InternalServerError      | 500                             | application/json                |
| errors.BadGatewayError          | 502                             | application/json                |
| errors.ServiceUnavailableError  | 503                             | application/json                |
| errors.GatewayTimeoutError      | 504                             | application/json                |
| errors.SDKDefaultError          | 4XX, 5XX                        | \*/\*                           |