# GlobalEventRules.Rulesets

## Overview

### Available Operations

* [create](#create) - Create Ruleset
* [delete](#delete) - Delete GER Ruleset
* [get](#get) - Get Ruleset
* [update](#update) - Update Ruleset

## create

Create a GER Ruleset.

### Example Usage

<!-- UsageSnippet language="python" operationID="GlobalEventRules_createRuleset" method="post" path="/v3/global-event-rules/{ger_id}/rulesets" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.global_event_rules.rulesets.create(ger_id=216762, alert_source_shortname="<value>", alert_source_version="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `ger_id`                                                                                      | *int*                                                                                         | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `alert_source_shortname`                                                                      | *str*                                                                                         | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `alert_source_version`                                                                        | *str*                                                                                         | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `catch_all_action`                                                                            | [Optional[models.V3GlobalEventRulesRuleAction]](../../models/v3globaleventrulesruleaction.md) | :heavy_minus_sign:                                                                            | N/A                                                                                           |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.GlobalEventRulesCreateRulesetResponse](../../models/globaleventrulescreaterulesetresponse.md)**

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

## delete

Delete a GER Ruleset

### Example Usage

<!-- UsageSnippet language="python" operationID="GlobalEventRules_deleteGerRuleset" method="delete" path="/v3/global-event-rules/{ger_id}/rulesets/{alert_source_version}/{alert_source_shortname}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.global_event_rules.rulesets.delete(ger_id=198518, alert_source_version="<value>", alert_source_shortname="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ger_id`                                                            | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `alert_source_version`                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `alert_source_shortname`                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
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

## get

Get a GER Ruleset

### Example Usage

<!-- UsageSnippet language="python" operationID="GlobalEventRules_getRuleset" method="get" path="/v3/global-event-rules/{ger_id}/rulesets/{alert_source_version}/{alert_source_shortname}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.global_event_rules.rulesets.get(ger_id=294223, alert_source_version="<value>", alert_source_shortname="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ger_id`                                                            | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `alert_source_version`                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `alert_source_shortname`                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GlobalEventRulesGetRulesetResponse](../../models/globaleventrulesgetrulesetresponse.md)**

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

Update a GER Ruleset

### Example Usage

<!-- UsageSnippet language="python" operationID="GlobalEventRules_updateRuleset" method="patch" path="/v3/global-event-rules/{ger_id}/rulesets/{alert_source_version}/{alert_source_shortname}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.global_event_rules.rulesets.update(ger_id=489958, alert_source_version="<value>", alert_source_shortname="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `ger_id`                                                                                                  | *int*                                                                                                     | :heavy_check_mark:                                                                                        | N/A                                                                                                       |
| `alert_source_version`                                                                                    | *str*                                                                                                     | :heavy_check_mark:                                                                                        | N/A                                                                                                       |
| `alert_source_shortname`                                                                                  | *str*                                                                                                     | :heavy_check_mark:                                                                                        | N/A                                                                                                       |
| `catch_all_action`                                                                                        | [Optional[models.V3GlobalEventRulesRuleActionUpdate]](../../models/v3globaleventrulesruleactionupdate.md) | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |

### Response

**[models.GlobalEventRulesUpdateRulesetResponse](../../models/globaleventrulesupdaterulesetresponse.md)**

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