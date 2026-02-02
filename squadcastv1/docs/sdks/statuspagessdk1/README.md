# StatusPages

## Overview

### Available Operations

* [list](#list) - List Status Pages
* [create](#create) - Create Status Page
* [delete_by_id](#delete_by_id) - Delete Status Page By ID
* [get_by_id](#get_by_id) - Get Status Page By ID
* [update](#update) - Update Status Page By ID
* [list_statuses](#list_statuses) - List Status Page Statuses

## list

List Status Pages

### Example Usage

<!-- UsageSnippet language="python" operationID="StatusPages_listStatusPages" method="get" path="/v4/statuspages" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.status_pages.list(page_size=301790, page_number=172386, filters_is_public="<value>", team_id="<id>")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `page_size`                                                         | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `page_number`                                                       | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `filters_is_public`                                                 | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `team_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.StatusPagesListStatusPagesResponse](../../models/statuspagesliststatuspagesresponse.md)**

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

Create Status Page

### Example Usage

<!-- UsageSnippet language="python" operationID="StatusPages_createStatusPage" method="post" path="/v4/statuspages" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.status_pages.create(name="<value>", domain_name="failing-convection.com", logo_url="https://snarling-season.info", timezone="Pacific/Chuuk", team_id="<id>", contact_email="<value>", owner_type="team", owner_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                             | Type                                                                                                                  | Required                                                                                                              | Description                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `name`                                                                                                                | *str*                                                                                                                 | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `domain_name`                                                                                                         | *str*                                                                                                                 | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `logo_url`                                                                                                            | *str*                                                                                                                 | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `timezone`                                                                                                            | *str*                                                                                                                 | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `team_id`                                                                                                             | *str*                                                                                                                 | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `contact_email`                                                                                                       | *str*                                                                                                                 | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `owner_type`                                                                                                          | [models.V4StatusPagesCreateStatusPageRequestOwnerType](../../models/v4statuspagescreatestatuspagerequestownertype.md) | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `owner_id`                                                                                                            | *str*                                                                                                                 | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `description`                                                                                                         | *Optional[str]*                                                                                                       | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `is_public`                                                                                                           | *Optional[bool]*                                                                                                      | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `custom_domain_name`                                                                                                  | *Optional[str]*                                                                                                       | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `theme_color`                                                                                                         | [Optional[models.V4StatusPagesNewStatusPageThemeColor]](../../models/v4statuspagesnewstatuspagethemecolor.md)         | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `components`                                                                                                          | List[[models.V4StatusPagesNewStatusPageComponentList](../../models/v4statuspagesnewstatuspagecomponentlist.md)]       | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `allow_webhook_subscription`                                                                                          | *Optional[bool]*                                                                                                      | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `allow_components_subscription`                                                                                       | *Optional[bool]*                                                                                                      | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `allow_maintenance_subscription`                                                                                      | *Optional[bool]*                                                                                                      | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `retries`                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                      | :heavy_minus_sign:                                                                                                    | Configuration to override the default retry behavior of the client.                                                   |

### Response

**[models.StatusPagesCreateStatusPageResponse](../../models/statuspagescreatestatuspageresponse.md)**

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

## delete_by_id

Delete Status Page By ID

### Example Usage

<!-- UsageSnippet language="python" operationID="StatusPages_deleteStatusPageById" method="delete" path="/v4/statuspages/{statuspageID}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.status_pages.delete_by_id(statuspage_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `statuspage_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.StatusPagesDeleteStatusPageByIDResponse](../../models/statuspagesdeletestatuspagebyidresponse.md)**

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

Get Status Page By ID

### Example Usage

<!-- UsageSnippet language="python" operationID="StatusPages_getStatusPageById" method="get" path="/v4/statuspages/{statuspageID}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.status_pages.get_by_id(statuspage_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `statuspage_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.StatusPagesGetStatusPageByIDResponse](../../models/statuspagesgetstatuspagebyidresponse.md)**

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

Update Status Page By ID

### Example Usage

<!-- UsageSnippet language="python" operationID="StatusPages_updateStatusPageById" method="put" path="/v4/statuspages/{statuspageID}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.status_pages.update(statuspage_id="<id>", name="<value>", is_public=False, domain_name="blank-brief.info", team_id="<id>", theme_color={
        "primary": "<value>",
        "secondary": "<value>",
    }, contact_email="<value>", owner_type="<value>", owner_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                             | Type                                                                                                                                  | Required                                                                                                                              | Description                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `statuspage_id`                                                                                                                       | *str*                                                                                                                                 | :heavy_check_mark:                                                                                                                    | N/A                                                                                                                                   |
| `name`                                                                                                                                | *str*                                                                                                                                 | :heavy_check_mark:                                                                                                                    | N/A                                                                                                                                   |
| `is_public`                                                                                                                           | *bool*                                                                                                                                | :heavy_check_mark:                                                                                                                    | N/A                                                                                                                                   |
| `domain_name`                                                                                                                         | *str*                                                                                                                                 | :heavy_check_mark:                                                                                                                    | N/A                                                                                                                                   |
| `team_id`                                                                                                                             | *str*                                                                                                                                 | :heavy_check_mark:                                                                                                                    | N/A                                                                                                                                   |
| `theme_color`                                                                                                                         | [models.V4StatusPagesUpdateStatusPageByIDRequestThemeColor](../../models/v4statuspagesupdatestatuspagebyidrequestthemecolor.md)       | :heavy_check_mark:                                                                                                                    | N/A                                                                                                                                   |
| `contact_email`                                                                                                                       | *str*                                                                                                                                 | :heavy_check_mark:                                                                                                                    | N/A                                                                                                                                   |
| `owner_type`                                                                                                                          | *str*                                                                                                                                 | :heavy_check_mark:                                                                                                                    | N/A                                                                                                                                   |
| `owner_id`                                                                                                                            | *str*                                                                                                                                 | :heavy_check_mark:                                                                                                                    | N/A                                                                                                                                   |
| `description`                                                                                                                         | *Optional[str]*                                                                                                                       | :heavy_minus_sign:                                                                                                                    | N/A                                                                                                                                   |
| `custom_domain_name`                                                                                                                  | *Optional[str]*                                                                                                                       | :heavy_minus_sign:                                                                                                                    | N/A                                                                                                                                   |
| `logo_url`                                                                                                                            | *Optional[str]*                                                                                                                       | :heavy_minus_sign:                                                                                                                    | N/A                                                                                                                                   |
| `timezone`                                                                                                                            | *Optional[str]*                                                                                                                       | :heavy_minus_sign:                                                                                                                    | N/A                                                                                                                                   |
| `allow_components_subscription`                                                                                                       | *Optional[bool]*                                                                                                                      | :heavy_minus_sign:                                                                                                                    | N/A                                                                                                                                   |
| `allow_maintenance_subscription`                                                                                                      | *Optional[bool]*                                                                                                                      | :heavy_minus_sign:                                                                                                                    | N/A                                                                                                                                   |
| `allow_webhook_subscription`                                                                                                          | *Optional[bool]*                                                                                                                      | :heavy_minus_sign:                                                                                                                    | N/A                                                                                                                                   |
| `components`                                                                                                                          | List[[models.V4StatusPagesUpdateStatusPageByIDRequestComponent2](../../models/v4statuspagesupdatestatuspagebyidrequestcomponent2.md)] | :heavy_minus_sign:                                                                                                                    | N/A                                                                                                                                   |
| `is_custom_domain_enabled`                                                                                                            | *Optional[bool]*                                                                                                                      | :heavy_minus_sign:                                                                                                                    | N/A                                                                                                                                   |
| `hide_from_search_engines`                                                                                                            | *Optional[bool]*                                                                                                                      | :heavy_minus_sign:                                                                                                                    | N/A                                                                                                                                   |
| `retries`                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                      | :heavy_minus_sign:                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                   |

### Response

**[models.StatusPagesUpdateStatusPageByIDResponse](../../models/statuspagesupdatestatuspagebyidresponse.md)**

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

## list_statuses

List Status Page Statuses

### Example Usage

<!-- UsageSnippet language="python" operationID="StatusPages_listStatusPageStatuses" method="get" path="/v4/statuspages/{statuspageID}/status" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.status_pages.list_statuses(statuspage_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `statuspage_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.StatusPagesListStatusPageStatusesResponse](../../models/statuspagesliststatuspagestatusesresponse.md)**

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