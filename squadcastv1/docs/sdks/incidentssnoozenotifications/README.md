# Incidents.SnoozeNotifications

## Overview

### Available Operations

* [unsnooze](#unsnooze) - Unsnooze Incident Notifications

## unsnooze

Unsnooze Incident Notifications

### Example Usage

<!-- UsageSnippet language="python" operationID="SnoozeNotifications_unsnoozeIncidentNotifications" method="put" path="/v3/incidents/{incidentID}/unsnooze" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.incidents.snooze_notifications.unsnooze(incident_id="<id>", reassign_to={
        "id": "<id>",
        "type": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                   | Type                                                                                                        | Required                                                                                                    | Description                                                                                                 |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `incident_id`                                                                                               | *str*                                                                                                       | :heavy_check_mark:                                                                                          | N/A                                                                                                         |
| `reassign_to`                                                                                               | [models.V3IncidentsSnoozeNotificationsReassignTo](../../models/v3incidentssnoozenotificationsreassignto.md) | :heavy_check_mark:                                                                                          | N/A                                                                                                         |
| `retries`                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                            | :heavy_minus_sign:                                                                                          | Configuration to override the default retry behavior of the client.                                         |

### Response

**[models.SnoozeNotificationsUnsnoozeIncidentNotificationsResponse](../../models/snoozenotificationsunsnoozeincidentnotificationsresponse.md)**

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