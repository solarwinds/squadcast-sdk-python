# Schedules

## Overview

### Available Operations

* [list](#list) - List Schedules
* [create](#create) - Create Schedule
* [delete](#delete) - Delete Schedule
* [get_by_id](#get_by_id) - Get Schedule by ID
* [update](#update) - Update Schedule
* [pause_resume](#pause_resume) - Pause/Resume Schedule
* [change_timezone](#change_timezone) - Change Timezone
* [clone](#clone) - Clone Schedule
* [get_ical_link](#get_ical_link) - Get Schedule ICal Link
* [create_ical_link](#create_ical_link) - Create Schedule ICal Link

## list

List Schedules

### Example Usage

<!-- UsageSnippet language="python" operationID="Schedules_listSchedules" method="get" path="/v4/schedules" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.schedules.list(team_id="<id>")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `team_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `schedule_i_ds`                                                     | List[*int*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `participants`                                                      | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `schedule_name`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `my_on_call`                                                        | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `you_and_your_squads`                                               | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `search`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `hide_paused`                                                       | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `owner_id`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `escalation_policies`                                               | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `without_escalation_policy`                                         | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `cursor`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SchedulesListSchedulesResponse](../../models/scheduleslistschedulesresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.CommonV4Error              | 400, 401, 402, 403, 404, 409, 422 | application/json                  |
| errors.CommonV4Error              | 500, 502, 503, 504                | application/json                  |
| errors.SDKDefaultError            | 4XX, 5XX                          | \*/\*                             |

## create

Create Schedule

### Example Usage

<!-- UsageSnippet language="python" operationID="Schedules_createSchedule" method="post" path="/v4/schedules" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.schedules.create(name="<value>", description="fumigate pfft kooky whoa but lighthearted popularity", team_id="<id>", owner_id="<id>", owner_type="user", time_zone="Pacific/Easter", tags=[
        {
            "key": "<key>",
            "value": "<value>",
            "color": "pink",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `name`                                                                                      | *str*                                                                                       | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `description`                                                                               | *str*                                                                                       | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `team_id`                                                                                   | *str*                                                                                       | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `owner_id`                                                                                  | *str*                                                                                       | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `owner_type`                                                                                | [models.V4CreateScheduleRequestOwnerType](../../models/v4createschedulerequestownertype.md) | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `time_zone`                                                                                 | *str*                                                                                       | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `tags`                                                                                      | List[[models.V4Tag](../../models/v4tag.md)]                                                 | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.SchedulesCreateScheduleResponse](../../models/schedulescreatescheduleresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.CommonV4Error              | 400, 401, 402, 403, 404, 409, 422 | application/json                  |
| errors.CommonV4Error              | 500, 502, 503, 504                | application/json                  |
| errors.SDKDefaultError            | 4XX, 5XX                          | \*/\*                             |

## delete

Delete Schedule

### Example Usage

<!-- UsageSnippet language="python" operationID="Schedules_deleteSchedule" method="delete" path="/v4/schedules/{scheduleID}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.schedules.delete(schedule_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `schedule_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[bytes](../../models/.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.CommonV4Error              | 400, 401, 402, 403, 404, 409, 422 | application/json                  |
| errors.CommonV4Error              | 500, 502, 503, 504                | application/json                  |
| errors.SDKDefaultError            | 4XX, 5XX                          | \*/\*                             |

## get_by_id

Get Schedule by ID

### Example Usage

<!-- UsageSnippet language="python" operationID="Schedules_getScheduleById" method="get" path="/v4/schedules/{scheduleID}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.schedules.get_by_id(schedule_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `schedule_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SchedulesGetScheduleByIDResponse](../../models/schedulesgetschedulebyidresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.CommonV4Error              | 400, 401, 402, 403, 404, 409, 422 | application/json                  |
| errors.CommonV4Error              | 500, 502, 503, 504                | application/json                  |
| errors.SDKDefaultError            | 4XX, 5XX                          | \*/\*                             |

## update

Update Schedule

### Example Usage

<!-- UsageSnippet language="python" operationID="Schedules_updateSchedule" method="put" path="/v4/schedules/{scheduleID}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.schedules.update(schedule_id="<id>", name="<value>", description="smoothly festival unruly alert now far provided absentmindedly", owner_id="<id>", owner_type="squad", tags=[])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `schedule_id`                                                                               | *str*                                                                                       | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `name`                                                                                      | *str*                                                                                       | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `description`                                                                               | *str*                                                                                       | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `owner_id`                                                                                  | *str*                                                                                       | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `owner_type`                                                                                | [models.V4UpdateScheduleRequestOwnerType](../../models/v4updateschedulerequestownertype.md) | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `tags`                                                                                      | List[[models.V4Tag](../../models/v4tag.md)]                                                 | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.SchedulesUpdateScheduleResponse](../../models/schedulesupdatescheduleresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.CommonV4Error              | 400, 401, 402, 403, 404, 409, 422 | application/json                  |
| errors.CommonV4Error              | 500, 502, 503, 504                | application/json                  |
| errors.SDKDefaultError            | 4XX, 5XX                          | \*/\*                             |

## pause_resume

Pause/Resume Schedule

### Example Usage

<!-- UsageSnippet language="python" operationID="Schedules_pauseresumeSchedule" method="patch" path="/v4/schedules/{scheduleID}/actions" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.schedules.pause_resume(schedule_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `schedule_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `action`                                                            | [Optional[models.Action]](../../models/action.md)                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SchedulesPauseresumeScheduleResponse](../../models/schedulespauseresumescheduleresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.CommonV4Error              | 400, 401, 402, 403, 404, 409, 422 | application/json                  |
| errors.CommonV4Error              | 500, 502, 503, 504                | application/json                  |
| errors.SDKDefaultError            | 4XX, 5XX                          | \*/\*                             |

## change_timezone

Change Timezone

### Example Usage

<!-- UsageSnippet language="python" operationID="Schedules_changeTimezone" method="patch" path="/v4/schedules/{scheduleID}/change-timezone" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.schedules.change_timezone(schedule_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `schedule_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `time_zone`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SchedulesChangeTimezoneResponse](../../models/scheduleschangetimezoneresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.CommonV4Error              | 400, 401, 402, 403, 404, 409, 422 | application/json                  |
| errors.CommonV4Error              | 500, 502, 503, 504                | application/json                  |
| errors.SDKDefaultError            | 4XX, 5XX                          | \*/\*                             |

## clone

Clone Schedule

### Example Usage

<!-- UsageSnippet language="python" operationID="Schedules_cloneSchedule" method="post" path="/v4/schedules/{scheduleID}/clone" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.schedules.clone(schedule_id="<id>", request_body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `schedule_id`                                                                                 | *str*                                                                                         | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `request_body`                                                                                | [models.SchedulesCloneScheduleRequestBody](../../models/schedulescloneschedulerequestbody.md) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.SchedulesCloneScheduleResponse](../../models/schedulesclonescheduleresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.CommonV4Error              | 400, 401, 402, 403, 404, 409, 422 | application/json                  |
| errors.CommonV4Error              | 500, 502, 503, 504                | application/json                  |
| errors.SDKDefaultError            | 4XX, 5XX                          | \*/\*                             |

## get_ical_link

Get Schedule ICal Link

### Example Usage

<!-- UsageSnippet language="python" operationID="Export_getScheduleIcalLink" method="get" path="/v4/schedules/{scheduleID}/ical-link" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.schedules.get_ical_link(schedule_id="<id>", my_on_call=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `schedule_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `my_on_call`                                                        | *bool*                                                              | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ExportGetScheduleIcalLinkResponse](../../models/exportgetscheduleicallinkresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.CommonV4Error              | 400, 401, 402, 403, 404, 409, 422 | application/json                  |
| errors.CommonV4Error              | 500, 502, 503, 504                | application/json                  |
| errors.SDKDefaultError            | 4XX, 5XX                          | \*/\*                             |

## create_ical_link

Create Schedule ICal Link

### Example Usage

<!-- UsageSnippet language="python" operationID="Export_createScheduleIcalLink" method="post" path="/v4/schedules/{scheduleID}/ical-link" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.schedules.create_ical_link(schedule_id="<id>", my_on_call=True, request_body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `schedule_id`                                                                                             | *str*                                                                                                     | :heavy_check_mark:                                                                                        | N/A                                                                                                       |
| `my_on_call`                                                                                              | *bool*                                                                                                    | :heavy_check_mark:                                                                                        | N/A                                                                                                       |
| `request_body`                                                                                            | [models.ExportCreateScheduleIcalLinkRequestBody](../../models/exportcreatescheduleicallinkrequestbody.md) | :heavy_check_mark:                                                                                        | N/A                                                                                                       |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |

### Response

**[models.ExportCreateScheduleIcalLinkResponse](../../models/exportcreatescheduleicallinkresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.CommonV4Error              | 400, 401, 402, 403, 404, 409, 422 | application/json                  |
| errors.CommonV4Error              | 500, 502, 503, 504                | application/json                  |
| errors.SDKDefaultError            | 4XX, 5XX                          | \*/\*                             |