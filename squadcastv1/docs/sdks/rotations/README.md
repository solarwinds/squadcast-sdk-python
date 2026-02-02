# Rotations

## Overview

### Available Operations

* [list_by_schedule](#list_by_schedule) - List Schedule Rotations
* [create](#create) - Create Rotation
* [delete](#delete) - Delete Rotation
* [get_by_id](#get_by_id) - Get Schedule Rotation by ID
* [update](#update) - Update Rotation
* [get_participants](#get_participants) - Get Rotation Participants
* [update_participants](#update_participants) - Update Rotation Participants

## list_by_schedule

List Schedule Rotations

### Example Usage

<!-- UsageSnippet language="python" operationID="Rotations_getScheduleRotations" method="get" path="/v4/schedules/{scheduleID}/rotations" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.rotations.list_by_schedule(schedule_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `schedule_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RotationsGetScheduleRotationsResponse](../../models/rotationsgetschedulerotationsresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.CommonV4Error              | 400, 401, 402, 403, 404, 409, 422 | application/json                  |
| errors.CommonV4Error              | 500, 502, 503, 504                | application/json                  |
| errors.SDKDefaultError            | 4XX, 5XX                          | \*/\*                             |

## create

Create Rotation

### Example Usage

<!-- UsageSnippet language="python" operationID="Rotations_createRotation" method="post" path="/v4/schedules/{scheduleID}/rotations" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.rotations.create(schedule_id="<id>", name="<value>", start_date="<value>", period="<value>", change_participants_frequency=62013, change_participants_unit="<value>", participant_groups=[])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `schedule_id`                                                         | *str*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `name`                                                                | *str*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `start_date`                                                          | *str*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `period`                                                              | *str*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `change_participants_frequency`                                       | *int*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `change_participants_unit`                                            | *str*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `participant_groups`                                                  | List[[models.V4ParticipantGroup](../../models/v4participantgroup.md)] | :heavy_check_mark:                                                    | N/A                                                                   |
| `color`                                                               | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `custom_period_frequency`                                             | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `custom_period_unit`                                                  | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `shift_time_slots`                                                    | List[[models.V4ShiftTimeSlot](../../models/v4shifttimeslot.md)]       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `end_date`                                                            | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `ends_after_iterations`                                               | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | N/A                                                                   |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.RotationsCreateRotationResponse](../../models/rotationscreaterotationresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.CommonV4Error              | 400, 401, 402, 403, 404, 409, 422 | application/json                  |
| errors.CommonV4Error              | 500, 502, 503, 504                | application/json                  |
| errors.SDKDefaultError            | 4XX, 5XX                          | \*/\*                             |

## delete

Delete Rotation

### Example Usage

<!-- UsageSnippet language="python" operationID="Rotations_deleteRotation" method="delete" path="/v4/schedules/{scheduleID}/rotations/{rotationID}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.rotations.delete(schedule_id="<id>", rotation_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `schedule_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `rotation_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
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

Get Schedule Rotation by ID

### Example Usage

<!-- UsageSnippet language="python" operationID="Rotations_getScheduleRotationById" method="get" path="/v4/schedules/{scheduleID}/rotations/{rotationID}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.rotations.get_by_id(schedule_id="<id>", rotation_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `schedule_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `rotation_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RotationsGetScheduleRotationByIDResponse](../../models/rotationsgetschedulerotationbyidresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.CommonV4Error              | 400, 401, 402, 403, 404, 409, 422 | application/json                  |
| errors.CommonV4Error              | 500, 502, 503, 504                | application/json                  |
| errors.SDKDefaultError            | 4XX, 5XX                          | \*/\*                             |

## update

Update Rotation

### Example Usage

<!-- UsageSnippet language="python" operationID="Rotations_updateRotation" method="put" path="/v4/schedules/{scheduleID}/rotations/{rotationID}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.rotations.update(schedule_id="<id>", rotation_id="<id>", name="<value>", start_date="<value>", period="<value>", change_participants_frequency=183098, change_participants_unit="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `schedule_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `rotation_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `start_date`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `period`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `change_participants_frequency`                                     | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `change_participants_unit`                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `color`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `custom_period_frequency`                                           | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `custom_period_unit`                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `shift_time_slots`                                                  | List[[models.V4ShiftTimeSlot](../../models/v4shifttimeslot.md)]     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `end_date`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `ends_after_iterations`                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RotationsUpdateRotationResponse](../../models/rotationsupdaterotationresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.CommonV4Error              | 400, 401, 402, 403, 404, 409, 422 | application/json                  |
| errors.CommonV4Error              | 500, 502, 503, 504                | application/json                  |
| errors.SDKDefaultError            | 4XX, 5XX                          | \*/\*                             |

## get_participants

Get Rotation Participants

### Example Usage

<!-- UsageSnippet language="python" operationID="Rotations_getRotationParticipants" method="get" path="/v4/schedules/{scheduleID}/rotations/{rotationID}/participants" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.rotations.get_participants(schedule_id="<id>", rotation_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `schedule_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `rotation_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RotationsGetRotationParticipantsResponse](../../models/rotationsgetrotationparticipantsresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.CommonV4Error              | 400, 401, 402, 403, 404, 409, 422 | application/json                  |
| errors.CommonV4Error              | 500, 502, 503, 504                | application/json                  |
| errors.SDKDefaultError            | 4XX, 5XX                          | \*/\*                             |

## update_participants

Update Rotation Participants

### Example Usage

<!-- UsageSnippet language="python" operationID="Rotations_updateRotationParticipants" method="put" path="/v4/schedules/{scheduleID}/rotations/{rotationID}/participants" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.rotations.update_participants(schedule_id="<id>", rotation_id="<id>", participant_groups=[])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `schedule_id`                                                         | *str*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `rotation_id`                                                         | *str*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `participant_groups`                                                  | List[[models.V4ParticipantGroup](../../models/v4participantgroup.md)] | :heavy_check_mark:                                                    | N/A                                                                   |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.RotationsUpdateRotationParticipantsResponse](../../models/rotationsupdaterotationparticipantsresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.CommonV4Error              | 400, 401, 402, 403, 404, 409, 422 | application/json                  |
| errors.CommonV4Error              | 500, 502, 503, 504                | application/json                  |
| errors.SDKDefaultError            | 4XX, 5XX                          | \*/\*                             |