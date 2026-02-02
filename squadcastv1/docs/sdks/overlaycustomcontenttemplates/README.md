# Services.Overlay.CustomContentTemplates

## Overview

### Available Operations

* [get_all](#get_all) - Get All Custom Content Template Overlay by Service
* [create_or_update](#create_or_update) - Create or Update Notification Template Overlay

## get_all

Get All Custom Content Template Overlay by Service

### Example Usage

<!-- UsageSnippet language="python" operationID="Overlay_getAllCustomContentTemplateOverlayByService" method="get" path="/v3/services/{serviceID}/overlays/custom-content" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.services.overlay.custom_content_templates.get_all(service_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `service_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.OverlayGetAllCustomContentTemplateOverlayByServiceResponse](../../models/overlaygetallcustomcontenttemplateoverlaybyserviceresponse.md)**

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

## create_or_update

Create or Update Notification Template Overlay

### Example Usage

<!-- UsageSnippet language="python" operationID="Overlay_createOrUpdateNotificationTemplateOverlay" method="put" path="/v3/services/{serviceID}/overlays/custom-content/{alertSource}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.services.overlay.custom_content_templates.create_or_update(service_id="<id>", alert_source="<value>", overlay_template_type="<value>", message_overlay={
        "template": "<value>",
    }, description_overlay={
        "template": "<value>",
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
| `message_overlay`                                                   | [models.MessageOverlay](../../models/messageoverlay.md)             | :heavy_check_mark:                                                  | N/A                                                                 |
| `description_overlay`                                               | [models.DescriptionOverlay](../../models/descriptionoverlay.md)     | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.OverlayCreateOrUpdateNotificationTemplateOverlayResponse](../../models/overlaycreateorupdatenotificationtemplateoverlayresponse.md)**

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