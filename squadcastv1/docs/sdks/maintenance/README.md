# Services.Maintenance

## Overview

### Available Operations

* [create_or_update](#create_or_update) - Create or Update Maintenance Mode

## create_or_update

Create or Update Maintenance Mode

### Example Usage

<!-- UsageSnippet language="python" operationID="MaintenanceMode_createOrUpdateMaintenanceMode" method="post" path="/v3/services/{serviceID}/maintenance" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.services.maintenance.create_or_update(service_id="<id>", on_maintenance=True, service_maintenance=[
        {
            "maintenance_start_date": "<value>",
            "daily": False,
            "weekly": True,
            "two_weekly": False,
            "three_weekly": True,
            "monthly": True,
            "deleted": False,
            "repeat_till": "<value>",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                               | Type                                                                                                                    | Required                                                                                                                | Description                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `service_id`                                                                                                            | *str*                                                                                                                   | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `on_maintenance`                                                                                                        | *bool*                                                                                                                  | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `service_maintenance`                                                                                                   | List[[models.V3ServicesMaintenanceModeServiceMaintenance](../../models/v3servicesmaintenancemodeservicemaintenance.md)] | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `retries`                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                        | :heavy_minus_sign:                                                                                                      | Configuration to override the default retry behavior of the client.                                                     |

### Response

**[models.MaintenanceModeCreateOrUpdateMaintenanceModeResponse](../../models/maintenancemodecreateorupdatemaintenancemoderesponse.md)**

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