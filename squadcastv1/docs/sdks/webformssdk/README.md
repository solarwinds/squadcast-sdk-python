# Webforms

## Overview

### Available Operations

* [list](#list) - Get All Webforms
* [create](#create) - Create Webform
* [update](#update) - Update Webform
* [remove](#remove) - Remove Webform
* [get_by_id](#get_by_id) - Get Webform By ID

## list

Returns all webforms of the given `owner_id` (teamId) in the request param.
Requires `access_token` as a `Bearer {{token}}` in the `Authorization` header with `read` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="Webforms_getAllWebforms" method="get" path="/v3/webform" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.webforms.list(owner_id="<id>")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `owner_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `page_number`                                                       | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.WebformsGetAllWebformsResponse](../../models/webformsgetallwebformsresponse.md)**

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

## create

Add a webform to the organization. Returns the webform object in response.
Requires `access_token` as a `Bearer {{token}}` in the `Authorization` header with `user-write` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="Webforms_createWebform" method="post" path="/v3/webform" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.webforms.create(owner_id="<id>", name="<value>", is_cname=False, is_captcha_enabled=False, captcha_secret={
        "site_key": "<value>",
        "secret": "<value>",
    }, form_owner_type="<value>", form_owner_id="<id>", services=[], header="<value>", title="<value>", footer_text="<value>", footer_link="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                 | Type                                                                                                                      | Required                                                                                                                  | Description                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `owner_id`                                                                                                                | *str*                                                                                                                     | :heavy_check_mark:                                                                                                        | Unique identifier of the owner (string or UUID)                                                                           |
| `name`                                                                                                                    | *str*                                                                                                                     | :heavy_check_mark:                                                                                                        | Name of the webform                                                                                                       |
| `is_cname`                                                                                                                | *bool*                                                                                                                    | :heavy_check_mark:                                                                                                        | Indicates if a custom domain (CNAME) is used                                                                              |
| `is_captcha_enabled`                                                                                                      | *bool*                                                                                                                    | :heavy_check_mark:                                                                                                        | Whether CAPTCHA is enabled on the form                                                                                    |
| `captcha_secret`                                                                                                          | [models.V3WebformsRecaptchaSecrets](../../models/v3webformsrecaptchasecrets.md)                                           | :heavy_check_mark:                                                                                                        | CAPTCHA credentials to be validated                                                                                       |
| `form_owner_type`                                                                                                         | *str*                                                                                                                     | :heavy_check_mark:                                                                                                        | Entity type that owns the form (e.g., team, user)                                                                         |
| `form_owner_id`                                                                                                           | *str*                                                                                                                     | :heavy_check_mark:                                                                                                        | Identifier for the owner entity                                                                                           |
| `services`                                                                                                                | List[[models.V3WebformsWFService](../../models/v3webformswfservice.md)]                                                   | :heavy_check_mark:                                                                                                        | List of services tied to this webform                                                                                     |
| `header`                                                                                                                  | *str*                                                                                                                     | :heavy_check_mark:                                                                                                        | Header text shown on the form                                                                                             |
| `title`                                                                                                                   | *str*                                                                                                                     | :heavy_check_mark:                                                                                                        | Title of the webform                                                                                                      |
| `footer_text`                                                                                                             | *str*                                                                                                                     | :heavy_check_mark:                                                                                                        | Text displayed in the footer                                                                                              |
| `footer_link`                                                                                                             | *str*                                                                                                                     | :heavy_check_mark:                                                                                                        | Hyperlink in the footer (mailto or https)                                                                                 |
| `host_name`                                                                                                               | *Optional[str]*                                                                                                           | :heavy_minus_sign:                                                                                                        | Custom hostname if CNAME is enabled                                                                                       |
| `tags`                                                                                                                    | [Optional[models.V3WebformsCreateOrUpdateWebformRequestTags]](../../models/v3webformscreateorupdatewebformrequesttags.md) | :heavy_minus_sign:                                                                                                        | Key-value tags for the webform                                                                                            |
| `input_field`                                                                                                             | List[[models.V3WebformsWFInputField](../../models/v3webformswfinputfield.md)]                                             | :heavy_minus_sign:                                                                                                        | Input fields to be rendered on the form                                                                                   |
| `logo_url`                                                                                                                | *Optional[str]*                                                                                                           | :heavy_minus_sign:                                                                                                        | URL to the organization's logo                                                                                            |
| `email_on`                                                                                                                | List[*str*]                                                                                                               | :heavy_minus_sign:                                                                                                        | Emails to notify on submission                                                                                            |
| `description`                                                                                                             | *Optional[str]*                                                                                                           | :heavy_minus_sign:                                                                                                        | Optional description for the webform                                                                                      |
| `retries`                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                          | :heavy_minus_sign:                                                                                                        | Configuration to override the default retry behavior of the client.                                                       |

### Response

**[models.WebformsCreateWebformResponse](../../models/webformscreatewebformresponse.md)**

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

Update a webform to the organization. Returns the webform object in response.
Requires `access_token` as a `Bearer {{token}}` in the `Authorization` header with `user-write` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="Webforms_updateWebform" method="put" path="/v3/webform/{webformId}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.webforms.update(webform_id=926692, owner_id="<id>", name="<value>", is_cname=True, is_captcha_enabled=True, captcha_secret={
        "site_key": "<value>",
        "secret": "<value>",
    }, form_owner_type="<value>", form_owner_id="<id>", services=[
        {
            "service_id": "<id>",
            "name": "<value>",
            "alias": "<value>",
        },
    ], header="<value>", title="<value>", footer_text="<value>", footer_link="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                 | Type                                                                                                                      | Required                                                                                                                  | Description                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `webform_id`                                                                                                              | *int*                                                                                                                     | :heavy_check_mark:                                                                                                        | N/A                                                                                                                       |
| `owner_id`                                                                                                                | *str*                                                                                                                     | :heavy_check_mark:                                                                                                        | Unique identifier of the owner (string or UUID)                                                                           |
| `name`                                                                                                                    | *str*                                                                                                                     | :heavy_check_mark:                                                                                                        | Name of the webform                                                                                                       |
| `is_cname`                                                                                                                | *bool*                                                                                                                    | :heavy_check_mark:                                                                                                        | Indicates if a custom domain (CNAME) is used                                                                              |
| `is_captcha_enabled`                                                                                                      | *bool*                                                                                                                    | :heavy_check_mark:                                                                                                        | Whether CAPTCHA is enabled on the form                                                                                    |
| `captcha_secret`                                                                                                          | [models.V3WebformsRecaptchaSecrets](../../models/v3webformsrecaptchasecrets.md)                                           | :heavy_check_mark:                                                                                                        | CAPTCHA credentials to be validated                                                                                       |
| `form_owner_type`                                                                                                         | *str*                                                                                                                     | :heavy_check_mark:                                                                                                        | Entity type that owns the form (e.g., team, user)                                                                         |
| `form_owner_id`                                                                                                           | *str*                                                                                                                     | :heavy_check_mark:                                                                                                        | Identifier for the owner entity                                                                                           |
| `services`                                                                                                                | List[[models.V3WebformsWFService](../../models/v3webformswfservice.md)]                                                   | :heavy_check_mark:                                                                                                        | List of services tied to this webform                                                                                     |
| `header`                                                                                                                  | *str*                                                                                                                     | :heavy_check_mark:                                                                                                        | Header text shown on the form                                                                                             |
| `title`                                                                                                                   | *str*                                                                                                                     | :heavy_check_mark:                                                                                                        | Title of the webform                                                                                                      |
| `footer_text`                                                                                                             | *str*                                                                                                                     | :heavy_check_mark:                                                                                                        | Text displayed in the footer                                                                                              |
| `footer_link`                                                                                                             | *str*                                                                                                                     | :heavy_check_mark:                                                                                                        | Hyperlink in the footer (mailto or https)                                                                                 |
| `host_name`                                                                                                               | *Optional[str]*                                                                                                           | :heavy_minus_sign:                                                                                                        | Custom hostname if CNAME is enabled                                                                                       |
| `tags`                                                                                                                    | [Optional[models.V3WebformsCreateOrUpdateWebformRequestTags]](../../models/v3webformscreateorupdatewebformrequesttags.md) | :heavy_minus_sign:                                                                                                        | Key-value tags for the webform                                                                                            |
| `input_field`                                                                                                             | List[[models.V3WebformsWFInputField](../../models/v3webformswfinputfield.md)]                                             | :heavy_minus_sign:                                                                                                        | Input fields to be rendered on the form                                                                                   |
| `logo_url`                                                                                                                | *Optional[str]*                                                                                                           | :heavy_minus_sign:                                                                                                        | URL to the organization's logo                                                                                            |
| `email_on`                                                                                                                | List[*str*]                                                                                                               | :heavy_minus_sign:                                                                                                        | Emails to notify on submission                                                                                            |
| `description`                                                                                                             | *Optional[str]*                                                                                                           | :heavy_minus_sign:                                                                                                        | Optional description for the webform                                                                                      |
| `retries`                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                          | :heavy_minus_sign:                                                                                                        | Configuration to override the default retry behavior of the client.                                                       |

### Response

**[models.WebformsUpdateWebformResponse](../../models/webformsupdatewebformresponse.md)**

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

## remove

Remove a webform from the organization.
Requires `access_token` as a `Bearer {{token}}` in the `Authorization` header with `user-write` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="Webforms_removeWebform" method="delete" path="/v3/webform/{webformId}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.webforms.remove(webform_id=842504, owner_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `webform_id`                                                        | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `owner_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.WebformsRemoveWebformResponse](../../models/webformsremovewebformresponse.md)**

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

Returns a webform details of the given `webformId` in the request param.
Requires `access_token` as a `Bearer {{token}}` in the `Authorization` header with `read` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="Webforms_getWebformById" method="get" path="/v3/webform/{webformId}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.webforms.get_by_id(webform_id=831002, owner_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `webform_id`                                                        | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `owner_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.WebformsGetWebformByIDResponse](../../models/webformsgetwebformbyidresponse.md)**

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