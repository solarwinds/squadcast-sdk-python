# Slos

## Overview

### Available Operations

* [list_all](#list_all) - Get All SLOs
* [create](#create) - Create SLO
* [update](#update) - Update SLO
* [remove](#remove) - Remove SLO
* [get](#get) - Get SLO By ID
* [mark_affected](#mark_affected) - Mark SLO Affected

## list_all

Returns all the SLOs of the passed owner_id in the params.
Requires `access_token` as a `Bearer {{token}}` in the `Authorization` header with `read` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="SLO_getAllSLOs" method="get" path="/v3/slo" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.slos.list_all(owner_id="<id>", offset="<value>", limit="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `owner_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `offset`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `limit`                                                             | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SLOGetAllSLOsResponse](../../models/slogetallslosresponse.md)**

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

- This API will create SLO.
Requires `access_token` as a `Bearer {{token}}` in the `Authorization` header with `user-write` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="SLO_createSLO" method="post" path="/v3/slo" -->
```python
from squadcast_sdk import SquadcastSDK
from squadcast_sdk.utils import parse_datetime


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.slos.create(name="<value>", time_interval_type="rolling", service_ids=[
        "<value 1>",
    ], slis=[], target_slo=6924.37, start_time=parse_datetime("2023-06-03T10:41:05.981Z"), end_time=parse_datetime("2023-11-20T07:09:22.422Z"), duration_in_days=574042, owner_type="<value>", owner_id="<id>", slo_owner_id="<id>", slo_owner_type="squad")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `name`                                                                                  | *str*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `time_interval_type`                                                                    | [models.V3SLOTimeIntervalType](../../models/v3slotimeintervaltype.md)                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `service_ids`                                                                           | List[*str*]                                                                             | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `slis`                                                                                  | List[*str*]                                                                             | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `target_slo`                                                                            | *float*                                                                                 | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `start_time`                                                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects)                    | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `end_time`                                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects)                    | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `duration_in_days`                                                                      | *int*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `owner_type`                                                                            | *str*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `owner_id`                                                                              | *str*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `slo_owner_id`                                                                          | *str*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `slo_owner_type`                                                                        | [models.V3SLOSLOOwnerType](../../models/v3slosloownertype.md)                           | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `description`                                                                           | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `tags`                                                                                  | [Optional[models.V3SLOCreateSLORequestTags]](../../models/v3slocreateslorequesttags.md) | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `slo_monitoring_checks`                                                                 | List[[models.V3SLOSLOMonitoringCheck](../../models/v3sloslomonitoringcheck.md)]         | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `slo_actions`                                                                           | List[[models.V3SLOSLOAction](../../models/v3slosloaction.md)]                           | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.SLOCreateSLOResponse](../../models/slocreatesloresponse.md)**

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

## update

- This API will update SLO.
Requires `access_token` as a `Bearer {{token}}` in the `Authorization` header with `user-write` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="SLO_updateSLO" method="put" path="/v3/slo/{sloID}" -->
```python
from squadcast_sdk import SquadcastSDK
from squadcast_sdk.utils import parse_datetime


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.slos.update(slo_id=16112, owner_id_param="<value>", name="<value>", time_interval_type="rolling", service_ids=[
        "<value 1>",
        "<value 2>",
        "<value 3>",
    ], slis=[
        "<value 1>",
    ], target_slo=2464.03, start_time=parse_datetime("2025-10-31T03:29:37.701Z"), end_time=parse_datetime("2024-03-30T19:04:36.297Z"), duration_in_days=271064, owner_type="<value>", owner_id="<id>", slo_owner_id="<id>", slo_owner_type="user")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `slo_id`                                                                                | *int*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `owner_id_param`                                                                        | *str*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `name`                                                                                  | *str*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `time_interval_type`                                                                    | [models.V3SLOTimeIntervalType](../../models/v3slotimeintervaltype.md)                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `service_ids`                                                                           | List[*str*]                                                                             | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `slis`                                                                                  | List[*str*]                                                                             | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `target_slo`                                                                            | *float*                                                                                 | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `start_time`                                                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects)                    | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `end_time`                                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects)                    | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `duration_in_days`                                                                      | *int*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `owner_type`                                                                            | *str*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `owner_id`                                                                              | *str*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `slo_owner_id`                                                                          | *str*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `slo_owner_type`                                                                        | [models.V3SLOSLOOwnerType](../../models/v3slosloownertype.md)                           | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `description`                                                                           | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `tags`                                                                                  | [Optional[models.V3SLOCreateSLORequestTags]](../../models/v3slocreateslorequesttags.md) | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `slo_monitoring_checks`                                                                 | List[[models.V3SLOSLOMonitoringCheck](../../models/v3sloslomonitoringcheck.md)]         | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `slo_actions`                                                                           | List[[models.V3SLOSLOAction](../../models/v3slosloaction.md)]                           | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.SLOUpdateSLOResponse](../../models/sloupdatesloresponse.md)**

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

## remove

Remove SLO from passed owner_id (team_id) in the params . Upon sccess the slo will be removed.
Requires `access_token` as a `Bearer {{token}}` in the `Authorization` header with `user-write` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="SLO_removeSLO" method="delete" path="/v3/slo/{sloID}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.slos.remove(slo_id=938544, owner_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `slo_id`                                                            | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `owner_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SLORemoveSLOResponse](../../models/sloremovesloresponse.md)**

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

## get

Returns a SLO details of the given `sloID` in the request param.
Requires `access_token` as a `Bearer {{token}}` in the `Authorization` header with `read` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="SLO_getSLOById" method="get" path="/v3/slo/{sloID}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.slos.get(slo_id=586718, owner_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `slo_id`                                                            | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `owner_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SLOGetSLOByIDResponse](../../models/slogetslobyidresponse.md)**

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

## mark_affected

This endpoint is used for mark slo affected.

Requires `access_token` as a `Bearer {{token}}` in the `Authorization` header with `user-write` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="SLO_markSLOAffected" method="post" path="/v3/slo/{sloID}/incident" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.slos.mark_affected(slo_id=294670, owner_id_param="<value>", incident_id="<id>", slis=[
        "<value 1>",
        "<value 2>",
    ], error_budget_spent=3480.26, owner_type="<value>", owner_id="<id>", org_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `slo_id`                                                            | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `owner_id_param`                                                    | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `incident_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `slis`                                                              | List[*str*]                                                         | :heavy_check_mark:                                                  | N/A                                                                 |
| `error_budget_spent`                                                | *float*                                                             | :heavy_check_mark:                                                  | N/A                                                                 |
| `owner_type`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `owner_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `org_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SLOMarkSLOAffectedResponse](../../models/slomarksloaffectedresponse.md)**

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