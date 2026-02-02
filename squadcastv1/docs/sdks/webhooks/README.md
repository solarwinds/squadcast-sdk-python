# Webhooks

## Overview

### Available Operations

* [create](#create) - Create Webhook
* [delete](#delete) - Delete Webhook
* [get_by_id](#get_by_id) - Get Webhook By ID
* [update](#update) - Update Webhook

## create

Add webhook to the organization. Returns the webhook object in response.
Requires `access_token` as a `Bearer {{token}}` in the `Authorization` header with `user-write` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="Webhooks_createWebhook" method="post" path="/v3/extensions/event-webhooks" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.webhooks.create(name="<value>", triggers=[], urls=[
        {},
    ], trigger_type="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                       | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `name`                                                                                                          | *str*                                                                                                           | :heavy_check_mark:                                                                                              | Name of the webhook                                                                                             |
| `triggers`                                                                                                      | List[[models.V3ExtensionsWebhooksWebhookTrigger](../../models/v3extensionswebhookswebhooktrigger.md)]           | :heavy_check_mark:                                                                                              | A list of triggers for this webhook                                                                             |
| `urls`                                                                                                          | List[[models.V3ExtensionsWebhooksWebhookURL](../../models/v3extensionswebhookswebhookurl.md)]                   | :heavy_check_mark:                                                                                              | A list of URLs to which the webhook payload will be sent                                                        |
| `trigger_type`                                                                                                  | *str*                                                                                                           | :heavy_check_mark:                                                                                              | Type of trigger                                                                                                 |
| `description`                                                                                                   | *Optional[str]*                                                                                                 | :heavy_minus_sign:                                                                                              | Description of the webhook                                                                                      |
| `header`                                                                                                        | [OptionalNullable[models.V3ExtensionsWebhooksWebhookHeader]](../../models/v3extensionswebhookswebhookheader.md) | :heavy_minus_sign:                                                                                              | Headers to be sent with the webhook                                                                             |
| `filters`                                                                                                       | [OptionalNullable[models.V3ExtensionsWebhooksWebhookFilter]](../../models/v3extensionswebhookswebhookfilter.md) | :heavy_minus_sign:                                                                                              | Filters to apply to the webhook                                                                                 |
| `max_retry`                                                                                                     | *Optional[int]*                                                                                                 | :heavy_minus_sign:                                                                                              | Maximum number of retries for the webhook                                                                       |
| `teams`                                                                                                         | List[*str*]                                                                                                     | :heavy_minus_sign:                                                                                              | List of team IDs to which this webhook is applicable                                                            |
| `is_all_teams_configured`                                                                                       | *Optional[bool]*                                                                                                | :heavy_minus_sign:                                                                                              | Set to true if the webhook is configured for all teams                                                          |
| `custom_payload_template_slug`                                                                                  | *Optional[str]*                                                                                                 | :heavy_minus_sign:                                                                                              | Slug of the custom payload template                                                                             |
| `language`                                                                                                      | *Optional[str]*                                                                                                 | :heavy_minus_sign:                                                                                              | Language for the webhook payload                                                                                |
| `mail_ids`                                                                                                      | List[*str*]                                                                                                     | :heavy_minus_sign:                                                                                              | List of email IDs for notification                                                                              |
| `custom_payload`                                                                                                | *Optional[str]*                                                                                                 | :heavy_minus_sign:                                                                                              | Custom payload for the webhook                                                                                  |
| `payload_type`                                                                                                  | *Optional[str]*                                                                                                 | :heavy_minus_sign:                                                                                              | Type of payload                                                                                                 |
| `retries`                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                | :heavy_minus_sign:                                                                                              | Configuration to override the default retry behavior of the client.                                             |

### Response

**[models.WebhooksCreateWebhookResponse](../../models/webhookscreatewebhookresponse.md)**

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

Remove webhook from the organization. Upon success, the webhook will be removed from the organization.
Requires `access_token` as a `Bearer {{token}}` in the `Authorization` header with `user-write` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="Webhooks_deleteWebhook" method="delete" path="/v3/extensions/event-webhooks/{eventWebhookID}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.webhooks.delete(event_webhook_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `event_webhook_id`                                                  | *str*                                                               | :heavy_check_mark:                                                  | (Required) event webhook ID                                         |
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

## get_by_id

Returns a webhooks details of the given `eventWebhookID` in the request param.
Requires `access_token` as a `Bearer {{token}}` in the `Authorization` header with `read` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="Webhooks_getWebhookById" method="get" path="/v3/extensions/event-webhooks/{eventWebhookID}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.webhooks.get_by_id(event_webhook_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `event_webhook_id`                                                  | *str*                                                               | :heavy_check_mark:                                                  | (Required) event webhook ID                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.WebhooksGetWebhookByIDResponse](../../models/webhooksgetwebhookbyidresponse.md)**

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

Update organization webhook details.
Requires `access_token` as a `Bearer {{token}}` in the `Authorization` header with `user-write` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="Webhooks_updateWebhook" method="put" path="/v3/extensions/event-webhooks/{eventWebhookID}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.webhooks.update(event_webhook_id="<id>", name="<value>", triggers=[
        {
            "event_class": "<value>",
            "event_type": "<value>",
        },
    ], urls=[
        {},
    ], trigger_type="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                       | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `event_webhook_id`                                                                                              | *str*                                                                                                           | :heavy_check_mark:                                                                                              | N/A                                                                                                             |
| `name`                                                                                                          | *str*                                                                                                           | :heavy_check_mark:                                                                                              | Name of the webhook                                                                                             |
| `triggers`                                                                                                      | List[[models.V3ExtensionsWebhooksWebhookTrigger](../../models/v3extensionswebhookswebhooktrigger.md)]           | :heavy_check_mark:                                                                                              | A list of triggers for this webhook                                                                             |
| `urls`                                                                                                          | List[[models.V3ExtensionsWebhooksWebhookURL](../../models/v3extensionswebhookswebhookurl.md)]                   | :heavy_check_mark:                                                                                              | A list of URLs to which the webhook payload will be sent                                                        |
| `trigger_type`                                                                                                  | *str*                                                                                                           | :heavy_check_mark:                                                                                              | Type of trigger                                                                                                 |
| `description`                                                                                                   | *Optional[str]*                                                                                                 | :heavy_minus_sign:                                                                                              | Description of the webhook                                                                                      |
| `header`                                                                                                        | [OptionalNullable[models.V3ExtensionsWebhooksWebhookHeader]](../../models/v3extensionswebhookswebhookheader.md) | :heavy_minus_sign:                                                                                              | Headers to be sent with the webhook                                                                             |
| `filters`                                                                                                       | [OptionalNullable[models.V3ExtensionsWebhooksWebhookFilter]](../../models/v3extensionswebhookswebhookfilter.md) | :heavy_minus_sign:                                                                                              | Filters to apply to the webhook                                                                                 |
| `max_retry`                                                                                                     | *Optional[int]*                                                                                                 | :heavy_minus_sign:                                                                                              | Maximum number of retries for the webhook                                                                       |
| `teams`                                                                                                         | List[*str*]                                                                                                     | :heavy_minus_sign:                                                                                              | List of team IDs to which this webhook is applicable                                                            |
| `is_all_teams_configured`                                                                                       | *Optional[bool]*                                                                                                | :heavy_minus_sign:                                                                                              | Set to true if the webhook is configured for all teams                                                          |
| `custom_payload_template_slug`                                                                                  | *Optional[str]*                                                                                                 | :heavy_minus_sign:                                                                                              | Slug of the custom payload template                                                                             |
| `language`                                                                                                      | *Optional[str]*                                                                                                 | :heavy_minus_sign:                                                                                              | Language for the webhook payload                                                                                |
| `mail_ids`                                                                                                      | List[*str*]                                                                                                     | :heavy_minus_sign:                                                                                              | List of email IDs for notification                                                                              |
| `custom_payload`                                                                                                | *Optional[str]*                                                                                                 | :heavy_minus_sign:                                                                                              | Custom payload for the webhook                                                                                  |
| `payload_type`                                                                                                  | *Optional[str]*                                                                                                 | :heavy_minus_sign:                                                                                              | Type of payload                                                                                                 |
| `retries`                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                | :heavy_minus_sign:                                                                                              | Configuration to override the default retry behavior of the client.                                             |

### Response

**[models.WebhooksUpdateWebhookResponse](../../models/webhooksupdatewebhookresponse.md)**

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