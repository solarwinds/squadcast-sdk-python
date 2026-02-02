# Services.Overlays

## Overview

### Available Operations

* [render_dedup_key](#render_dedup_key) - Render Dedup Key template

## render_dedup_key

Render Dedup Key template

### Example Usage

<!-- UsageSnippet language="python" operationID="Overlay_renderDedupKeyTemplate" method="post" path="/v3/services/{serviceID}/overlays/dedup-key/render" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.services.overlays.render_dedup_key(service_id="<id>", overlay_template_type="<value>", template="<value>", payload="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `service_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `overlay_template_type`                                             | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `template`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `payload`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.OverlayRenderDedupKeyTemplateResponse](../../models/overlayrenderdedupkeytemplateresponse.md)**

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