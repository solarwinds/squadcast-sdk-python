# Maintenances

## Overview

### Available Operations

* [delete](#delete) - Delete Maintenance By ID
* [update_by_id](#update_by_id) - Update Maintenance By ID

## delete

Delete Maintenance By ID

### Example Usage

<!-- UsageSnippet language="python" operationID="Maintenances_deleteMaintenanceById" method="delete" path="/v4/statuspages/{statuspageID}/maintenance/{maintenance_id}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.maintenances.delete(statuspage_id="<id>", maintenance_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `statuspage_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `maintenance_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.MaintenancesDeleteMaintenanceByIDResponse](../../models/maintenancesdeletemaintenancebyidresponse.md)**

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

## update_by_id

Update Maintenance By ID

### Example Usage

<!-- UsageSnippet language="python" operationID="Maintenances_updateMaintenanceById" method="put" path="/v4/statuspages/{statuspageID}/maintenance/{maintenance_id}" -->
```python
from squadcast_sdk import SquadcastSDK
from squadcast_sdk.utils import parse_datetime


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.maintenances.update_by_id(statuspage_id="<id>", maintenance_id="<id>", title="<value>", note="<value>", start_time=parse_datetime("2024-07-22T17:12:15.919Z"), end_time=parse_datetime("2024-06-11T21:00:35.262Z"))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `statuspage_id`                                                      | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `maintenance_id`                                                     | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `title`                                                              | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `note`                                                               | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `start_time`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `end_time`                                                           | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `components`                                                         | List[*int*]                                                          | :heavy_minus_sign:                                                   | N/A                                                                  |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |

### Response

**[models.MaintenancesUpdateMaintenanceByIDResponse](../../models/maintenancesupdatemaintenancebyidresponse.md)**

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