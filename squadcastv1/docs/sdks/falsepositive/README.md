# Slos.FalsePositive

## Overview

### Available Operations

* [mark](#mark) - Mark SLO False Positive

## mark

Value is a boolean (true or false)

### Example Usage

<!-- UsageSnippet language="python" operationID="SLO_markSLOFalsePositive" method="patch" path="/v3/slo/{sloID}/incident/{incidentID}/false-positive/{value}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.slos.false_positive.mark(slo_id=825843, incident_id=505067, value=True, owner_id="<id>", request_body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `slo_id`                                                                                        | *int*                                                                                           | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `incident_id`                                                                                   | *int*                                                                                           | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `value`                                                                                         | *bool*                                                                                          | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `owner_id`                                                                                      | *str*                                                                                           | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `request_body`                                                                                  | [models.SLOMarkSLOFalsePositiveRequestBody](../../models/slomarkslofalsepositiverequestbody.md) | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.SLOMarkSLOFalsePositiveResponse](../../models/slomarkslofalsepositiveresponse.md)**

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