# Services.Overlays.DedupKey

## Overview

### Available Operations

* [update](#update) - Update Dedup Key Overlay

## update

Update Dedup Key Overlay

### Example Usage

<!-- UsageSnippet language="python" operationID="Overlay_updateDedupKeyOverlay" method="put" path="/v3/services/{serviceID}/overlays/dedup-key/{alertSource}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.services.overlays.dedup_key.update(service_id="<id>", alert_source="<value>", overlay_template_type="<value>", dedup_key_overlay={
        "template": "<value>",
        "duration": 360400,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `service_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `alert_source`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `overlay_template_type`                                             | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `dedup_key_overlay`                                                 | [models.DedupKeyOverlay](../../models/dedupkeyoverlay.md)           | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.OverlayUpdateDedupKeyOverlayResponse](../../models/overlayupdatededupkeyoverlayresponse.md)**

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