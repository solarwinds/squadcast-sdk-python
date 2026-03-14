# Schedules.Overrides

## Overview

### Available Operations

* [list](#list) - List Overrides
* [create](#create) - Create Schedule Override
* [update](#update) - Update Schedule Override

## list

List Overrides

### Example Usage

<!-- UsageSnippet language="python" operationID="Overrides_listOverrides" method="get" path="/v4/schedules/{scheduleID}/overrides" -->
```python
from squadcast import SquadcastSDK


with SquadcastSDK(
    refresh_token_auth="<YOUR_REFRESH_TOKEN_AUTH_HERE>",
) as squadcast_sdk:

    res = squadcast_sdk.schedules.overrides.list(schedule_id="<id>", start_time="<value>", end_time="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `schedule_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `start_time`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `end_time`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `participant_id`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `cursor`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.OverridesListOverridesResponse](../../models/overrideslistoverridesresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.CommonV4Error              | 400, 401, 402, 403, 404, 409, 422 | application/json                  |
| errors.CommonV4Error              | 500, 502, 503, 504                | application/json                  |
| errors.SDKDefaultError            | 4XX, 5XX                          | \*/\*                             |

## create

Create Schedule Override

### Example Usage

<!-- UsageSnippet language="python" operationID="Overrides_createScheduleOverride" method="post" path="/v4/schedules/{scheduleID}/overrides" -->
```python
from squadcast import SquadcastSDK


with SquadcastSDK(
    refresh_token_auth="<YOUR_REFRESH_TOKEN_AUTH_HERE>",
) as squadcast_sdk:

    res = squadcast_sdk.schedules.overrides.create(schedule_id="<id>", start_time="<value>", end_time="<value>", reason="<value>", overridden_participant={
        "group": [
            {
                "id": "<id>",
                "type": "<value>",
            },
        ],
    }, override_with={
        "group": [
            {
                "id": "<id>",
                "type": "<value>",
            },
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `schedule_id`                                                                   | *str*                                                                           | :heavy_check_mark:                                                              | N/A                                                                             |
| `start_time`                                                                    | *str*                                                                           | :heavy_check_mark:                                                              | N/A                                                                             |
| `end_time`                                                                      | *str*                                                                           | :heavy_check_mark:                                                              | N/A                                                                             |
| `reason`                                                                        | *str*                                                                           | :heavy_check_mark:                                                              | N/A                                                                             |
| `overridden_participant`                                                        | [models.V4OverrideParticipantGroup](../../models/v4overrideparticipantgroup.md) | :heavy_check_mark:                                                              | N/A                                                                             |
| `override_with`                                                                 | [models.V4OverrideParticipantGroup](../../models/v4overrideparticipantgroup.md) | :heavy_check_mark:                                                              | N/A                                                                             |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.OverridesCreateScheduleOverrideResponse](../../models/overridescreatescheduleoverrideresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.CommonV4Error              | 400, 401, 402, 403, 404, 409, 422 | application/json                  |
| errors.CommonV4Error              | 500, 502, 503, 504                | application/json                  |
| errors.SDKDefaultError            | 4XX, 5XX                          | \*/\*                             |

## update

Update Schedule Override

### Example Usage

<!-- UsageSnippet language="python" operationID="Overrides_updateScheduleOverride" method="put" path="/v4/schedules/{scheduleID}/overrides/{overrideID}" -->
```python
from squadcast import SquadcastSDK


with SquadcastSDK(
    refresh_token_auth="<YOUR_REFRESH_TOKEN_AUTH_HERE>",
) as squadcast_sdk:

    res = squadcast_sdk.schedules.overrides.update(schedule_id="<id>", override_id="<id>", start_time="<value>", end_time="<value>", reason="<value>", overridden_participant={
        "group": [
            {
                "id": "<id>",
                "type": "<value>",
            },
        ],
    }, override_with={
        "group": [],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `schedule_id`                                                                   | *str*                                                                           | :heavy_check_mark:                                                              | N/A                                                                             |
| `override_id`                                                                   | *str*                                                                           | :heavy_check_mark:                                                              | N/A                                                                             |
| `start_time`                                                                    | *str*                                                                           | :heavy_check_mark:                                                              | N/A                                                                             |
| `end_time`                                                                      | *str*                                                                           | :heavy_check_mark:                                                              | N/A                                                                             |
| `reason`                                                                        | *str*                                                                           | :heavy_check_mark:                                                              | N/A                                                                             |
| `overridden_participant`                                                        | [models.V4OverrideParticipantGroup](../../models/v4overrideparticipantgroup.md) | :heavy_check_mark:                                                              | N/A                                                                             |
| `override_with`                                                                 | [models.V4OverrideParticipantGroup](../../models/v4overrideparticipantgroup.md) | :heavy_check_mark:                                                              | N/A                                                                             |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.OverridesUpdateScheduleOverrideResponse](../../models/overridesupdatescheduleoverrideresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.CommonV4Error              | 400, 401, 402, 403, 404, 409, 422 | application/json                  |
| errors.CommonV4Error              | 500, 502, 503, 504                | application/json                  |
| errors.SDKDefaultError            | 4XX, 5XX                          | \*/\*                             |