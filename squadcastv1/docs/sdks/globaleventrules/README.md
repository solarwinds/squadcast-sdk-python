# GlobalEventRules

## Overview

### Available Operations

* [list](#list) - List Global Event Rules
* [create_rule](#create_rule) - Create Global Event Rule
* [delete_by_id](#delete_by_id) - Delete Global Event Rule by ID
* [get_by_id](#get_by_id) - Get Global Event Rule by ID
* [update_by_id](#update_by_id) - Update Global Event Rule by ID

## list

Get a list of all GERs

### Example Usage

<!-- UsageSnippet language="python" operationID="GlobalEventRules_listGlobalEventRules" method="get" path="/v3/global-event-rules" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.global_event_rules.list(owner_id="<id>")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `owner_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `page_number`                                                       | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `filters_owner_id`                                                  | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `filters_search`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GlobalEventRulesListGlobalEventRulesResponse](../../models/globaleventruleslistglobaleventrulesresponse.md)**

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

## create_rule

Create a GER

### Example Usage

<!-- UsageSnippet language="python" operationID="GlobalEventRules_createGlobalEventRule" method="post" path="/v3/global-event-rules" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.global_event_rules.create_rule(name="<value>", description="majestically effector headline dampen eek middle like shrill", owner_id="<id>", entity_owner={
        "id": "<id>",
        "type": "user",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `name`                                                                                | *str*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `description`                                                                         | *str*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `owner_id`                                                                            | *str*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `entity_owner`                                                                        | [models.V3GlobalEventRulesEntityOwner](../../models/v3globaleventrulesentityowner.md) | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.GlobalEventRulesCreateGlobalEventRuleResponse](../../models/globaleventrulescreateglobaleventruleresponse.md)**

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

## delete_by_id

Delete a GER by its ID

### Example Usage

<!-- UsageSnippet language="python" operationID="GlobalEventRules_deleteGlobalEventRuleById" method="delete" path="/v3/global-event-rules/{ger_id}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.global_event_rules.delete_by_id(ger_id=491102)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ger_id`                                                            | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[bytes](../../models/.md)**

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

## get_by_id

Get a GER by its ID

### Example Usage

<!-- UsageSnippet language="python" operationID="GlobalEventRules_getGlobalEventRuleById" method="get" path="/v3/global-event-rules/{ger_id}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.global_event_rules.get_by_id(ger_id=292040)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ger_id`                                                            | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GlobalEventRulesGetGlobalEventRuleByIDResponse](../../models/globaleventrulesgetglobaleventrulebyidresponse.md)**

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

Update a GER by its ID

### Example Usage

<!-- UsageSnippet language="python" operationID="GlobalEventRules_updateGlobalEventRuleById" method="patch" path="/v3/global-event-rules/{ger_id}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.global_event_rules.update_by_id(ger_id=885894)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                   | Type                                                                                                        | Required                                                                                                    | Description                                                                                                 |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `ger_id`                                                                                                    | *int*                                                                                                       | :heavy_check_mark:                                                                                          | N/A                                                                                                         |
| `name`                                                                                                      | *Optional[str]*                                                                                             | :heavy_minus_sign:                                                                                          | N/A                                                                                                         |
| `description`                                                                                               | *Optional[str]*                                                                                             | :heavy_minus_sign:                                                                                          | N/A                                                                                                         |
| `entity_owner`                                                                                              | [Optional[models.V3GlobalEventRulesEntityOwnerUpdate]](../../models/v3globaleventrulesentityownerupdate.md) | :heavy_minus_sign:                                                                                          | N/A                                                                                                         |
| `retries`                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                            | :heavy_minus_sign:                                                                                          | Configuration to override the default retry behavior of the client.                                         |

### Response

**[models.GlobalEventRulesUpdateGlobalEventRuleByIDResponse](../../models/globaleventrulesupdateglobaleventrulebyidresponse.md)**

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