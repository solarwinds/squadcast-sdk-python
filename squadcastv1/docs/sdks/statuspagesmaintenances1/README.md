# StatusPages.Maintenances

## Overview

### Available Operations

* [list](#list) - List Maintenances
* [create](#create) - Create Maintenance

## list

List Maintenances

### Example Usage

<!-- UsageSnippet language="python" operationID="Maintenances_listMaintenances" method="get" path="/v4/statuspages/{statuspageID}/maintenance" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.status_pages.maintenances.list(statuspage_id="<id>", start_time="<value>", end_time="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `statuspage_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `start_time`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `end_time`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.V4StatusPagesMaintenancesListMaintenancesResponse](../../models/v4statuspagesmaintenanceslistmaintenancesresponse.md)**

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

Create Maintenance

### Example Usage

<!-- UsageSnippet language="python" operationID="Maintenances_createMaintenance" method="post" path="/v4/statuspages/{statuspageID}/maintenance" -->
```python
from squadcast_sdk import SquadcastSDK
from squadcast_sdk.utils import parse_datetime


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.status_pages.maintenances.create(statuspage_id="<id>", title="<value>", note="<value>", components=[
        191583,
        227211,
        362920,
    ], start_time=parse_datetime("2024-08-24T09:07:30.992Z"), end_time=parse_datetime("2024-04-27T16:39:01.283Z"))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `statuspage_id`                                                      | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `title`                                                              | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `note`                                                               | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `components`                                                         | List[*int*]                                                          | :heavy_check_mark:                                                   | N/A                                                                  |
| `start_time`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `end_time`                                                           | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |

### Response

**[models.MaintenancesCreateMaintenanceResponse](../../models/maintenancescreatemaintenanceresponse.md)**

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