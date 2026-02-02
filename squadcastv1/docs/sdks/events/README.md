# Incidents.Events

## Overview

### Available Operations

* [get](#get) - Get Incident Events

## get

- This endpoint is used to get all the deduped incident events details by either ID or number.
- Requires `access_token` as a `Bearer {{token}}` in the `Authorization` header.

Query Params:
```
offset - non zero value
limit - non zero value, maximum is 10
sort - sort it by either asc or desc
deduped - if set to true, it will return only the deduplicated events. if set to false, it will return only the non-deduplicated event, otherwise it will return all the events
```

### Example Usage

<!-- UsageSnippet language="python" operationID="Incidents_getIncidentEvents" method="get" path="/v3/incidents/{incidentID}/events" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.incidents.events.get(incident_id="<id>", offset="<value>", limit="<value>", sort="<value>", deduped="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                     | Type                                                                                                                                                          | Required                                                                                                                                                      | Description                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `incident_id`                                                                                                                                                 | *str*                                                                                                                                                         | :heavy_check_mark:                                                                                                                                            | N/A                                                                                                                                                           |
| `offset`                                                                                                                                                      | *str*                                                                                                                                                         | :heavy_check_mark:                                                                                                                                            | non zero value                                                                                                                                                |
| `limit`                                                                                                                                                       | *str*                                                                                                                                                         | :heavy_check_mark:                                                                                                                                            | non zero value, maximum is 10                                                                                                                                 |
| `sort`                                                                                                                                                        | *str*                                                                                                                                                         | :heavy_check_mark:                                                                                                                                            | sort it by either asc or desc                                                                                                                                 |
| `deduped`                                                                                                                                                     | *str*                                                                                                                                                         | :heavy_check_mark:                                                                                                                                            | if set to true, it will return only the deduped events.<br/><br/>if set to false, it will return only the non-deduped event.<br/><br/>otherwise it will return all the events |
| `retries`                                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                              | :heavy_minus_sign:                                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                                           |

### Response

**[models.IncidentsGetIncidentEventsResponse](../../models/incidentsgetincidenteventsresponse.md)**

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