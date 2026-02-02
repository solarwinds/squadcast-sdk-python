# Incidents.Export

## Overview

### Available Operations

* [export_async](#export_async) - Incident Export Async

## export_async

*   This is an async API, once the request is made the export will start in our workers. You will get a download link to your registered Email ID once the export is completed


### Payload

| Key | Value | Example |
| --- | --- | --- |
| type | csv / json | “csv” |
| start_time | Date in ISO Format | “2020-01-01T00:00:00.000Z” |
| end_time | Date in ISO Format | “2020-04-01T00:00:00.000Z” |
| owner_id | Team ID | “611262a9d5b4ea846b534a3f” |

### Incident Filters

| Key | Value | Example |
| --- | --- | --- |
| statuses | Array of triggered / resolved / acknowledged / suppressed | \[“triggered”, “acknowleged”\] |
| tags | Array of tags in format “KEY=VALUE” | \[“severity=high”, “severity=low”\] |
| sources | Array of Alert Source IDs | \[“6077f7225fdc7075e371685f”\] |
| services | Array of Service IDs | \["62385fb309bc474014180828"\] |
| assigned_to | Array of Assigned to user IDs | \["625e40c9a9bd76370bf9f7fb"\] |

### Example Usage

<!-- UsageSnippet language="python" operationID="Incidents_incidentExportAsync" method="post" path="/v3/incidents/export/async" -->
```python
from squadcast_sdk import SquadcastSDK
from squadcast_sdk.utils import parse_datetime


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.incidents.export.export_async(owner_id="<id>", type_="csv", start_time=parse_datetime("2024-12-29T12:56:54.559Z"), end_time=parse_datetime("2025-08-25T17:31:33.747Z"), incident_filters={
        "services": [],
        "sources": [],
        "service_owner": {
            "user_i_ds": [
                "<value 1>",
            ],
            "squad_i_ds": [
                "<value 1>",
                "<value 2>",
                "<value 3>",
            ],
        },
        "assigned_to": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "assigned_to_user_i_ds_and_their_squads": [
            "<value 1>",
            "<value 2>",
        ],
        "statuses": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "priority": [
            "P5",
        ],
        "tags": [],
        "notes": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `owner_id`                                                                                  | *str*                                                                                       | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `type`                                                                                      | [models.V3IncidentsExportFormat](../../models/v3incidentsexportformat.md)                   | :heavy_check_mark:                                                                          | Type of export, can be csv or json                                                          |
| `start_time`                                                                                | [date](https://docs.python.org/3/library/datetime.html#date-objects)                        | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `end_time`                                                                                  | [date](https://docs.python.org/3/library/datetime.html#date-objects)                        | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `incident_filters`                                                                          | [models.V3IncidentsExportIncidentsFilter](../../models/v3incidentsexportincidentsfilter.md) | :heavy_check_mark:                                                                          | Filter criteria for incidents in an export.                                                 |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

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