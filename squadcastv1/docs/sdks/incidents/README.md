# Incidents

## Overview

### Available Operations

* [bulk_acknowledge](#bulk_acknowledge) - Bulk Acknowledge Incidents
* [export_incidents](#export_incidents) - Incident Export
* [bulk_update_priority](#bulk_update_priority) - Bulk Incidents Priority Update
* [bulk_resolve](#bulk_resolve) - Bulk Resolve Incidents
* [get_by_id](#get_by_id) - Get Incident by ID
* [acknowledge](#acknowledge) - Acknowledge Incident
* [mark_slo_false_positive](#mark_slo_false_positive) - Mark Incident SLO False Positive
* [update_priority](#update_priority) - Incident Priority Update
* [reassign](#reassign) - Reassign Incident
* [resolve](#resolve) - Resolve Incident
* [get_status_by_request_ids](#get_status_by_request_ids) - Get Incidents Status By RequestIDs

## bulk_acknowledge

- This endpoint is used to bulk acknowledge the incident by IDs. The API can handle a maximum of 100 incident IDs in a single request with 10 such calls per minute."
- Requires `access_token` as a `Bearer {{token}}` in the `Authorization` header.

### Example Usage

<!-- UsageSnippet language="python" operationID="Incidents_bulkAcknowledgeIncidents" method="post" path="/v3/incidents/acknowledge" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.incidents.bulk_acknowledge(incident_ids=[
        "<value 1>",
        "<value 2>",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `incident_ids`                                                      | List[*str*]                                                         | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.IncidentsBulkAcknowledgeIncidentsResponse](../../models/incidentsbulkacknowledgeincidentsresponse.md)**

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

## export_incidents

- This endpoint is used to export the incident details into a `csv` or `json` file.
- Requires `access_token` as a `Bearer {{token}}` in the `Authorization` header.
- Header field/value: `Content-Type`: `text/csv`


Query Params:

```
type: csv or json
start_time: filter by date range
end_time: filter by date range
services: filter by services
sources: filter by alert sources
assigned_to: filter by assignee
status: filter by incident status
slo_affecting: filetr by slo affected
slos: filter by slos
tags: filter by tags key=value

 ```

### Example Usage

<!-- UsageSnippet language="python" operationID="Incidents_incidentExport" method="get" path="/v3/incidents/export" -->
```python
from squadcast_sdk import SquadcastSDK
from squadcast_sdk.utils import parse_datetime


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    ss_client.incidents.export_incidents(start_time=parse_datetime("2023-02-02T07:53:59.590Z"), end_time=parse_datetime("2023-02-03T13:28:22.839Z"), type_="csv", owner_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                         | Type                                                                                                                              | Required                                                                                                                          | Description                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `start_time`                                                                                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                              | :heavy_check_mark:                                                                                                                | N/A                                                                                                                               |
| `end_time`                                                                                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                              | :heavy_check_mark:                                                                                                                | N/A                                                                                                                               |
| `type`                                                                                                                            | [models.V3IncidentsExportFormat](../../models/v3incidentsexportformat.md)                                                         | :heavy_check_mark:                                                                                                                | Defines the format of the export.                                                                                                 |
| `owner_id`                                                                                                                        | *str*                                                                                                                             | :heavy_check_mark:                                                                                                                | N/A                                                                                                                               |
| `status`                                                                                                                          | List[*str*]                                                                                                                       | :heavy_minus_sign:                                                                                                                | N/A                                                                                                                               |
| `services`                                                                                                                        | List[*str*]                                                                                                                       | :heavy_minus_sign:                                                                                                                | N/A                                                                                                                               |
| `sources`                                                                                                                         | List[*str*]                                                                                                                       | :heavy_minus_sign:                                                                                                                | N/A                                                                                                                               |
| `assigned_to`                                                                                                                     | List[*str*]                                                                                                                       | :heavy_minus_sign:                                                                                                                | N/A                                                                                                                               |
| `assigned_to_user_i_ds_and_their_squads`                                                                                          | List[*str*]                                                                                                                       | :heavy_minus_sign:                                                                                                                | N/A                                                                                                                               |
| `service_owner`                                                                                                                   | *Optional[str]*                                                                                                                   | :heavy_minus_sign:                                                                                                                | N/A                                                                                                                               |
| `priority`                                                                                                                        | List[[models.V3IncidentsIncidentPriority](../../models/v3incidentsincidentpriority.md)]                                           | :heavy_minus_sign:                                                                                                                | N/A                                                                                                                               |
| `tags`                                                                                                                            | List[*str*]                                                                                                                       | :heavy_minus_sign:                                                                                                                | N/A                                                                                                                               |
| `slo_affecting`                                                                                                                   | [Optional[models.V3IncidentsIncidentExportRequestSloAffecting]](../../models/v3incidentsincidentexportrequestsloaffecting.md)     | :heavy_minus_sign:                                                                                                                | N/A                                                                                                                               |
| `slos`                                                                                                                            | List[*int*]                                                                                                                       | :heavy_minus_sign:                                                                                                                | N/A                                                                                                                               |
| `is_starred`                                                                                                                      | [Optional[models.V3IncidentsIncidentExportRequestIsStarred]](../../models/v3incidentsincidentexportrequestisstarred.md)           | :heavy_minus_sign:                                                                                                                | N/A                                                                                                                               |
| `text_filter`                                                                                                                     | *Optional[str]*                                                                                                                   | :heavy_minus_sign:                                                                                                                | N/A                                                                                                                               |
| `notes`                                                                                                                           | [Optional[models.V3IncidentsIncidentExportRequestNotes]](../../models/v3incidentsincidentexportrequestnotes.md)                   | :heavy_minus_sign:                                                                                                                | N/A                                                                                                                               |
| `retrospectives`                                                                                                                  | [Optional[models.V3IncidentsIncidentExportRequestRetrospectives]](../../models/v3incidentsincidentexportrequestretrospectives.md) | :heavy_minus_sign:                                                                                                                | N/A                                                                                                                               |
| `sort_by`                                                                                                                         | [Optional[models.V3IncidentsIncidentExportRequestSortBy]](../../models/v3incidentsincidentexportrequestsortby.md)                 | :heavy_minus_sign:                                                                                                                | N/A                                                                                                                               |
| `retries`                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                  | :heavy_minus_sign:                                                                                                                | Configuration to override the default retry behavior of the client.                                                               |

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
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

## bulk_update_priority

- This endpoint is used to bulk update incident priority.

- Requires `access_token` as a `Bearer {{token}}` in the `Authorization` header.

### Example Usage

<!-- UsageSnippet language="python" operationID="Incidents_bulkIncidentsPriorityUpdate" method="put" path="/v3/incidents/priority" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.incidents.bulk_update_priority(incident_ids=[], priority="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `incident_ids`                                                      | List[*str*]                                                         | :heavy_check_mark:                                                  | N/A                                                                 |
| `priority`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[bytes](../../models/.md)**

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

## bulk_resolve

- This endpoint is used to bulk resolve the incident by IDs. The API can handle a maximum of 100 incident IDs in a single request with 10 such calls per minute."
- Requires `access_token` as a `Bearer {{token}}` in the `Authorization` header.

### Example Usage

<!-- UsageSnippet language="python" operationID="Incidents_bulkResolveIncidents" method="post" path="/v3/incidents/resolve" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.incidents.bulk_resolve(incident_ids=[
        "<value 1>",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `incident_ids`                                                      | List[*str*]                                                         | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.IncidentsBulkResolveIncidentsResponse](../../models/incidentsbulkresolveincidentsresponse.md)**

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

## get_by_id

- This endpoint is used to get the incident details by ID.
- Requires `access_token` as a `Bearer {{token}}` in the `Authorization` header.

### Example Usage

<!-- UsageSnippet language="python" operationID="Incidents_getIncidentById" method="get" path="/v3/incidents/{incidentID}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.incidents.get_by_id(incident_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `incident_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.IncidentsGetIncidentByIDResponse](../../models/incidentsgetincidentbyidresponse.md)**

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

## acknowledge

- This endpoint is used to acknowledge the incident by ID.
- Requires `access_token` as a `Bearer {{token}}` in the `Authorization` header.

### Example Usage

<!-- UsageSnippet language="python" operationID="Incidents_acknowledgeIncident" method="post" path="/v3/incidents/{incidentID}/acknowledge" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.incidents.acknowledge(incident_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `incident_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.IncidentsAcknowledgeIncidentResponse](../../models/incidentsacknowledgeincidentresponse.md)**

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

## mark_slo_false_positive

- This endpoint is used to mark incident slo false positive.

- Requires `access_token` as a `Bearer {{token}}` in the `Authorization` header.

### Example Usage

<!-- UsageSnippet language="python" operationID="Incidents_markIncidentSloFalsePositive" method="patch" path="/v3/incidents/{incidentID}/mark-slo-incident-false-postive/{value}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.incidents.mark_slo_false_positive(incident_id="<id>", value="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `incident_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `value`                                                             | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.IncidentsMarkIncidentSloFalsePositiveResponse](../../models/incidentsmarkincidentslofalsepositiveresponse.md)**

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

## update_priority

- This endpoint is used to update incident priority by ID.

- Requires `access_token` as a `Bearer {{token}}` in the `Authorization` header.

### Example Usage

<!-- UsageSnippet language="python" operationID="Incidents_incidentPriorityUpdate" method="patch" path="/v3/incidents/{incidentID}/priority" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.incidents.update_priority(incident_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `incident_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `priority`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.IncidentsIncidentPriorityUpdateResponse](../../models/incidentsincidentpriorityupdateresponse.md)**

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

## reassign

- This endpoint is used to reassign the unresolved incident to any user or escalation policy or squads by ID.
- Requires `access_token` as a `Bearer {{token}}` in the `Authorization` header.
- `type` can be either `user` or `escalationpolicy` or `squad`

### Example Usage

<!-- UsageSnippet language="python" operationID="Incidents_reassignIncident" method="post" path="/v3/incidents/{incidentID}/reassign" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.incidents.reassign(incident_id="<id>", reassign_to={
        "id": "<id>",
        "type": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `incident_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `reassign_to`                                                       | [models.ReassignTo](../../models/reassignto.md)                     | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.IncidentsReassignIncidentResponse](../../models/incidentsreassignincidentresponse.md)**

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

## resolve

- This endpoint is used to resolve the incident by ID.

- Requires `access_token` as a `Bearer {{token}}` in the `Authorization` header.

- Resolution Reason is mandatory / optional based on the organization feature settings (Only for Premium and Enterprise Orgs) [Read more](https://support.squadcast.com/incidents-page/incidents-details#understanding-resolution-reason)

### Example Usage

<!-- UsageSnippet language="python" operationID="Incidents_resolveIncident" method="post" path="/v3/incidents/{incidentID}/resolve" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.incidents.resolve(incident_id="<id>", resolution_reason={
        "message": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `incident_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `resolution_reason`                                                 | [models.ResolutionReason](../../models/resolutionreason.md)         | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.IncidentsResolveIncidentResponse](../../models/incidentsresolveincidentresponse.md)**

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

## get_status_by_request_ids

- This endpoint is used to get the status of incidents given list of request_ids
- Requires `access_token` as a `Bearer {{token}}` in the `Authorization` header.

# Response
- The response contains the mapping from `request_ids` to incident status.
- `status` field can be one of - `suppressed`, `discarded`, `deduplicated`, `created`, `error`.
-  status is `error` if the `request_id` is invalid. Both `incident_id` and `event_id` field won't be present if `status` is `error`
-  status is `suppressed` if the incident was suppressed due to suppression rules.
-  status is `deduplicated` if the incident was deduplicated due to deduplication rules.
-  status is `discarded` if the incident was discarded due to some deduplication rule. `incident_id` field won't be present if `status` is `discarded`.
-  otherwise, the status is `created`

### Example Usage

<!-- UsageSnippet language="python" operationID="Incidents_getIncidentsStatusByRequestids" method="post" path="/v3/requests/status" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.incidents.get_status_by_request_ids(request_ids=[
        "<value 1>",
        "<value 2>",
        "<value 3>",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request_ids`                                                       | List[*str*]                                                         | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.IncidentsGetIncidentsStatusByRequestidsResponse](../../models/incidentsgetincidentsstatusbyrequestidsresponse.md)**

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