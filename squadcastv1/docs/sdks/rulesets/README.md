# Rulesets

## Overview

### Available Operations

* [reorder](#reorder) - Reorder Ruleset

## reorder

Reorder rules of a GER Ruleset

### Example Usage

<!-- UsageSnippet language="python" operationID="GlobalEventRules_reorderRuleset" method="patch" path="/v3/global-event-rules/{ger_id}/rulesets/{alert_source_version}/{alert_source_shortname}/priority" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.rulesets.reorder(ger_id=572014, alert_source_version="<value>", alert_source_shortname="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ger_id`                                                            | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `alert_source_version`                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `alert_source_shortname`                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `ordering`                                                          | List[*int*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GlobalEventRulesReorderRulesetResponse](../../models/globaleventrulesreorderrulesetresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |