# GlobalEventRules.Rulesets.Rules

## Overview

### Available Operations

* [list](#list) - List Ruleset Rules
* [create](#create) - Create Rule
* [get_by_id](#get_by_id) - Get Rule by ID
* [update_by_id](#update_by_id) - Update Rule by ID
* [reorder](#reorder) - Reorder Ruleset By Index

## list

Get all rules of a GER Ruleset.

### Example Usage

<!-- UsageSnippet language="python" operationID="GlobalEventRules_listRulesetRules" method="get" path="/v3/global-event-rules/{ger_id}/rulesets/{alert_source_version}/{alert_source_shortname}/rules" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.global_event_rules.rulesets.rules.list(ger_id=894010, alert_source_version="<value>", alert_source_shortname="<value>")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ger_id`                                                            | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `alert_source_version`                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `alert_source_shortname`                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `page_number`                                                       | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `filters_search`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GlobalEventRulesListRulesetRulesResponse](../../models/globaleventruleslistrulesetrulesresponse.md)**

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

Create a GER Ruleset Rule.

### Example Usage

<!-- UsageSnippet language="python" operationID="GlobalEventRules_createRule" method="post" path="/v3/global-event-rules/{ger_id}/rulesets/{alert_source_version}/{alert_source_shortname}/rules" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.global_event_rules.rulesets.rules.create(ger_id=934313, alert_source_version="<value>", alert_source_shortname="<value>", description="ha newsprint within beside scientific", expression="<value>", action={
        "route_to": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `ger_id`                                                                            | *int*                                                                               | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `alert_source_version`                                                              | *str*                                                                               | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `alert_source_shortname`                                                            | *str*                                                                               | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `description`                                                                       | *str*                                                                               | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `expression`                                                                        | *str*                                                                               | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `action`                                                                            | [models.V3GlobalEventRulesRuleAction](../../models/v3globaleventrulesruleaction.md) | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.GlobalEventRulesCreateRuleResponse](../../models/globaleventrulescreateruleresponse.md)**

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

Get a GER Ruleset Rule by its ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="GlobalEventRules_getRuleById" method="get" path="/v3/global-event-rules/{ger_id}/rulesets/{alert_source_version}/{alert_source_shortname}/rules/{rule_id}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.global_event_rules.rulesets.rules.get_by_id(ger_id=518804, alert_source_version="<value>", alert_source_shortname="<value>", rule_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ger_id`                                                            | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `alert_source_version`                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `alert_source_shortname`                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `rule_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GlobalEventRulesGetRuleByIDResponse](../../models/globaleventrulesgetrulebyidresponse.md)**

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

Update a GER Ruleset Rule by its ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="GlobalEventRules_updateRuleById" method="patch" path="/v3/global-event-rules/{ger_id}/rulesets/{alert_source_version}/{alert_source_shortname}/rules/{rule_id}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.global_event_rules.rulesets.rules.update_by_id(ger_id=140241, alert_source_version="<value>", alert_source_shortname="<value>", rule_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `ger_id`                                                                                                  | *int*                                                                                                     | :heavy_check_mark:                                                                                        | N/A                                                                                                       |
| `alert_source_version`                                                                                    | *str*                                                                                                     | :heavy_check_mark:                                                                                        | N/A                                                                                                       |
| `alert_source_shortname`                                                                                  | *str*                                                                                                     | :heavy_check_mark:                                                                                        | N/A                                                                                                       |
| `rule_id`                                                                                                 | *str*                                                                                                     | :heavy_check_mark:                                                                                        | N/A                                                                                                       |
| `description`                                                                                             | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `expression`                                                                                              | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `action`                                                                                                  | [Optional[models.V3GlobalEventRulesRuleActionUpdate]](../../models/v3globaleventrulesruleactionupdate.md) | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |

### Response

**[models.GlobalEventRulesUpdateRuleByIDResponse](../../models/globaleventrulesupdaterulebyidresponse.md)**

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

## reorder

Reorder a GER Ruleset Rule by its index in the ruleset.

### Example Usage

<!-- UsageSnippet language="python" operationID="GlobalEventRules_reorderRulesetByIndex" method="patch" path="/v3/global-event-rules/{ger_id}/rulesets/{alert_source_version}/{alert_source_shortname}/rules/{rule_id}/priority" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.global_event_rules.rulesets.rules.reorder(ger_id=281260, alert_source_version="<value>", alert_source_shortname="<value>", rule_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ger_id`                                                            | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `alert_source_version`                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `alert_source_shortname`                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `rule_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `shift_to`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `shift_index_by`                                                    | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GlobalEventRulesReorderRulesetByIndexResponse](../../models/globaleventrulesreorderrulesetbyindexresponse.md)**

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