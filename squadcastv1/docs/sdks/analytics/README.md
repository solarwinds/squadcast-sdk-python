# Analytics

## Overview

### Available Operations

* [get_org_analytics](#get_org_analytics) - Get Org level analytics
* [get_team](#get_team) - Get Team level analytics

## get_org_analytics

Get Org level analytics

### Example Usage

<!-- UsageSnippet language="python" operationID="Analytics_getOrgAnalytics" method="get" path="/v3/analyticsv2/organization" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.analytics.get_org_analytics(from_="<value>", to="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `from_`                                                             | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `to`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `team_id`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `user_id`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AnalyticsGetOrgAnalyticsResponse](../../models/analyticsgetorganalyticsresponse.md)**

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

## get_team

Get Team level analytics

### Example Usage

<!-- UsageSnippet language="python" operationID="Analytics_getTeamAnalytics" method="get" path="/v3/analyticsv2/team" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.analytics.get_team(owner_id="<id>", from_="<value>", to="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `owner_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `from_`                                                             | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `to`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `user_id`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `service_id`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AnalyticsGetTeamAnalyticsResponse](../../models/analyticsgetteamanalyticsresponse.md)**

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