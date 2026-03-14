# SnoozeNotifications

## Overview

### Available Operations

* [snooze](#snooze) - Snooze Incident Notifications

## snooze

Snooze Incident Notifications

### Example Usage

<!-- UsageSnippet language="python" operationID="SnoozeNotifications_snoozeIncidentNotifications" method="put" path="/v3/incidents/{incidentID}/snooze" -->
```python
from squadcast import SquadcastSDK


with SquadcastSDK(
    refresh_token_auth="<YOUR_REFRESH_TOKEN_AUTH_HERE>",
) as squadcast_sdk:

    res = squadcast_sdk.snooze_notifications.snooze(incident_id="<id>", snooze_duration_in_mins=42279)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `incident_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `snooze_duration_in_mins`                                           | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SnoozeNotificationsSnoozeIncidentNotificationsResponse](../../models/snoozenotificationssnoozeincidentnotificationsresponse.md)**

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