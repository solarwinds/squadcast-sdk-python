# Incidents.Actions

## Overview

### Available Operations

* [rebuild_circleci_project](#rebuild_circleci_project) - Rebuild a Project In CircleCI

## rebuild_circleci_project

Rebuild a Project In CircleCI

### Example Usage

<!-- UsageSnippet language="python" operationID="IncidentActions_rebuildAProjectInCircleci" method="post" path="/v3/incidents/{incidentID}/actions/circleci/rebuild/{buildNumber}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.incidents.actions.rebuild_circleci_project(incident_id="<id>", build_number="<value>", vcs_type="<value>", username="Dora.Waelchi", reponame="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `incident_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `build_number`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `vcs_type`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `username`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `reponame`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.IncidentActionsRebuildAProjectInCircleciResponse](../../models/incidentactionsrebuildaprojectincircleciresponse.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.ResponseBodyError1       | 400                             | application/json                |
| errors.ResponseBodyError2       | 400                             | application/json                |
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