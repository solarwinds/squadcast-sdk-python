# ExportSchedule

## Overview

### Available Operations

* [refresh_ical_link](#refresh_ical_link) - Refresh Schedule ICal Link

## refresh_ical_link

Refresh Schedule ICal Link

### Example Usage

<!-- UsageSnippet language="python" operationID="Export_refreshScheduleIcalLink" method="patch" path="/v4/schedules/{scheduleID}/ical-link" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.export_schedule.refresh_ical_link(schedule_id="<id>", my_on_call=True, request_body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                   | Type                                                                                                        | Required                                                                                                    | Description                                                                                                 |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `schedule_id`                                                                                               | *str*                                                                                                       | :heavy_check_mark:                                                                                          | N/A                                                                                                         |
| `my_on_call`                                                                                                | *bool*                                                                                                      | :heavy_check_mark:                                                                                          | N/A                                                                                                         |
| `request_body`                                                                                              | [models.ExportRefreshScheduleIcalLinkRequestBody](../../models/exportrefreshscheduleicallinkrequestbody.md) | :heavy_check_mark:                                                                                          | N/A                                                                                                         |
| `retries`                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                            | :heavy_minus_sign:                                                                                          | Configuration to override the default retry behavior of the client.                                         |

### Response

**[models.ExportRefreshScheduleIcalLinkResponse](../../models/exportrefreshscheduleicallinkresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.CommonV4Error              | 400, 401, 402, 403, 404, 409, 422 | application/json                  |
| errors.CommonV4Error              | 500, 502, 503, 504                | application/json                  |
| errors.SDKDefaultError            | 4XX, 5XX                          | \*/\*                             |