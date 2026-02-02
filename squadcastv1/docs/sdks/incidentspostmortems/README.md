# Incidents.Postmortems

## Overview

### Available Operations

* [remove](#remove) - Delete Postmortem By Incident
* [get_by_incident](#get_by_incident) - Get Postmortem By Incident
* [update_by_incident](#update_by_incident) - Update Postmortem By Incident

## remove

*   This endpoint is used to delete a postmortem by incident.
*   Requires `access_token` as a `Bearer {{token}}` in the `Authorization` header.

### Example Usage

<!-- UsageSnippet language="python" operationID="Postmortems_deletePostmortemByIncident" method="delete" path="/v3/incidents/{incidentID}/postmortem" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.incidents.postmortems.remove(incident_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `incident_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PostmortemsDeletePostmortemByIncidentResponse](../../models/postmortemsdeletepostmortembyincidentresponse.md)**

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

## get_by_incident

*   This endpoint is used to get a postmortem by incident.
*   Requires `access_token` as a `Bearer {{token}}` in the `Authorization` header.

### Example Usage

<!-- UsageSnippet language="python" operationID="Postmortems_getPostmortemByIncident" method="get" path="/v3/incidents/{incidentID}/postmortem" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.incidents.postmortems.get_by_incident(incident_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `incident_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PostmortemsGetPostmortemByIncidentResponse](../../models/postmortemsgetpostmortembyincidentresponse.md)**

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

## update_by_incident

- This endpoint is used to update a postmortem by incident.
- Requires `access_token` as a `Bearer {{token}}` in the `Authorization` header.

### Example Usage

<!-- UsageSnippet language="python" operationID="Postmortems_updatePostmortemByIncident" method="put" path="/v3/incidents/{incidentID}/postmortem" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.incidents.postmortems.update_by_incident(incident_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                           | Type                                                                                                                                | Required                                                                                                                            | Description                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `incident_id`                                                                                                                       | *str*                                                                                                                               | :heavy_check_mark:                                                                                                                  | N/A                                                                                                                                 |
| `owner_id`                                                                                                                          | *Optional[str]*                                                                                                                     | :heavy_minus_sign:                                                                                                                  | N/A                                                                                                                                 |
| `postmortem`                                                                                                                        | *Optional[str]*                                                                                                                     | :heavy_minus_sign:                                                                                                                  | N/A                                                                                                                                 |
| `follow_ups`                                                                                                                        | List[[models.V3IncidentsPostmortemsPostmortemFollowUp](../../models/v3incidentspostmortemspostmortemfollowup.md)]                   | :heavy_minus_sign:                                                                                                                  | N/A                                                                                                                                 |
| `new_attachments`                                                                                                                   | List[[models.V3IncidentsPostmortemsPostmortemAttachmentRequest](../../models/v3incidentspostmortemspostmortemattachmentrequest.md)] | :heavy_minus_sign:                                                                                                                  | N/A                                                                                                                                 |
| `title`                                                                                                                             | *Optional[str]*                                                                                                                     | :heavy_minus_sign:                                                                                                                  | N/A                                                                                                                                 |
| `status`                                                                                                                            | [Optional[models.V3IncidentsPostmortemsPostmortemStatus]](../../models/v3incidentspostmortemspostmortemstatus.md)                   | :heavy_minus_sign:                                                                                                                  | Represents the status of a postmortem.                                                                                              |
| `retries`                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                    | :heavy_minus_sign:                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                 |

### Response

**[models.PostmortemsUpdatePostmortemByIncidentResponse](../../models/postmortemsupdatepostmortembyincidentresponse.md)**

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