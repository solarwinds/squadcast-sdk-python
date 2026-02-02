# Services

## Overview

### Available Operations

* [get_all](#get_all) - Get All Services
* [create](#create) - Create Service
* [get_by_name](#get_by_name) - Get Services By Name
* [get_by_id](#get_by_id) - Get Service By ID
* [update](#update) - Update Service
* [delete](#delete) - Delete Service
* [update_apta_config](#update_apta_config) - Auto Pause Transient Alerts (APTA)
* [create_or_update_iag_config](#create_or_update_iag_config) - Intelligent Alert Grouping (IAG)
* [update_notification_delay_config](#update_notification_delay_config) - Delayed Notification Config

## get_all

Get All Services

### Example Usage

<!-- UsageSnippet language="python" operationID="Services_getServices" method="get" path="/v3/services" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.services.get_all(owner_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `owner_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `entity_owner`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `name`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ServicesGetServicesResponse](../../models/servicesgetservicesresponse.md)**

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

Create Service

### Example Usage

<!-- UsageSnippet language="python" operationID="Services_createService" method="post" path="/v3/services" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.services.create(owner_id="<id>", name="<value>", escalation_policy_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                             | Type                                                                                                                  | Required                                                                                                              | Description                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `owner_id`                                                                                                            | *str*                                                                                                                 | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `name`                                                                                                                | *str*                                                                                                                 | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `escalation_policy_id`                                                                                                | *str*                                                                                                                 | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `description`                                                                                                         | *Optional[str]*                                                                                                       | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `email_prefix`                                                                                                        | *Optional[str]*                                                                                                       | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `maintainer`                                                                                                          | [Optional[models.V3ServicesServiceMaintainer]](../../models/v3servicesservicemaintainer.md)                           | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `tags`                                                                                                                | List[[models.V3ServicesServiceTag](../../models/v3servicesservicetag.md)]                                             | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `auto_pause_transient_alerts_config`                                                                                  | [Optional[models.V3ServicesAPTAConfig]](../../models/v3servicesaptaconfig.md)                                         | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `intelligent_alerts_grouping_config`                                                                                  | [Optional[models.V3ServicesIAGConfig]](../../models/v3servicesiagconfig.md)                                           | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `delay_notification_config`                                                                                           | [Optional[models.V3ServicesNotificationDelayConfigRequest]](../../models/v3servicesnotificationdelayconfigrequest.md) | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `dedup_init_config`                                                                                                   | [Optional[models.V3ServicesDedupInitConfig]](../../models/v3servicesdedupinitconfig.md)                               | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `retries`                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                      | :heavy_minus_sign:                                                                                                    | Configuration to override the default retry behavior of the client.                                                   |

### Response

**[models.ServicesCreateServiceResponse](../../models/servicescreateserviceresponse.md)**

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

## get_by_name

Get Services By Name

### Example Usage

<!-- UsageSnippet language="python" operationID="Services_getServicesByName" method="get" path="/v3/services/by-name" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.services.get_by_name(name="<value>", owner_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `owner_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ServicesGetServicesByNameResponse](../../models/servicesgetservicesbynameresponse.md)**

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

Get Service By ID

### Example Usage

<!-- UsageSnippet language="python" operationID="Services_getServiceById" method="get" path="/v3/services/{serviceID}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.services.get_by_id(service_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `service_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ServicesGetServiceByIDResponse](../../models/servicesgetservicebyidresponse.md)**

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

Update Service

### Example Usage

<!-- UsageSnippet language="python" operationID="Services_updateService" method="put" path="/v3/services/{serviceID}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.services.update(service_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                             | Type                                                                                                                  | Required                                                                                                              | Description                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `service_id`                                                                                                          | *str*                                                                                                                 | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `name`                                                                                                                | *Optional[str]*                                                                                                       | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `escalation_policy_id`                                                                                                | *Optional[str]*                                                                                                       | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `description`                                                                                                         | *Optional[str]*                                                                                                       | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `email_prefix`                                                                                                        | *Optional[str]*                                                                                                       | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `maintainer`                                                                                                          | [Optional[models.V3ServicesServiceMaintainer]](../../models/v3servicesservicemaintainer.md)                           | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `tags`                                                                                                                | List[[models.V3ServicesServiceTag](../../models/v3servicesservicetag.md)]                                             | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `auto_pause_transient_alerts_config`                                                                                  | [Optional[models.V3ServicesAPTAConfig]](../../models/v3servicesaptaconfig.md)                                         | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `intelligent_alerts_grouping_config`                                                                                  | [Optional[models.V3ServicesIAGConfig]](../../models/v3servicesiagconfig.md)                                           | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `delay_notification_config`                                                                                           | [Optional[models.V3ServicesNotificationDelayConfigRequest]](../../models/v3servicesnotificationdelayconfigrequest.md) | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `retries`                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                      | :heavy_minus_sign:                                                                                                    | Configuration to override the default retry behavior of the client.                                                   |

### Response

**[models.ServicesUpdateServiceResponse](../../models/servicesupdateserviceresponse.md)**

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

Delete Service

### Example Usage

<!-- UsageSnippet language="python" operationID="Services_deleteService" method="delete" path="/v3/services/{serviceID}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.services.delete(service_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `service_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
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

## update_apta_config

Auto Pause Transient Alerts (APTA)

### Example Usage

<!-- UsageSnippet language="python" operationID="Services_createOrUpdateAPTAConfig" method="put" path="/v3/services/{serviceID}/apta-config" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.services.update_apta_config(service_id="<id>", is_enabled=False, timeout_in_mins=680029)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `service_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `is_enabled`                                                        | *bool*                                                              | :heavy_check_mark:                                                  | N/A                                                                 |
| `timeout_in_mins`                                                   | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ServicesCreateOrUpdateAPTAConfigResponse](../../models/servicescreateorupdateaptaconfigresponse.md)**

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

## create_or_update_iag_config

Intelligent Alert Grouping (IAG)

### Example Usage

<!-- UsageSnippet language="python" operationID="Services_createOrUpdateIAGConfig" method="put" path="/v3/services/{serviceID}/iag-config" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.services.create_or_update_iag_config(service_id="<id>", is_enabled=True, rolling_window_in_mins=246036)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `service_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `is_enabled`                                                        | *bool*                                                              | :heavy_check_mark:                                                  | N/A                                                                 |
| `rolling_window_in_mins`                                            | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ServicesCreateOrUpdateIAGConfigResponse](../../models/servicescreateorupdateiagconfigresponse.md)**

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

## update_notification_delay_config

Delayed Notification Config

### Example Usage

<!-- UsageSnippet language="python" operationID="Services_delayedNotificationConfig" method="put" path="/v3/services/{serviceID}/notification-delay-config" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.services.update_notification_delay_config(service_id="<id>", is_enabled=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                   | Type                                                                                                                                                        | Required                                                                                                                                                    | Description                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `service_id`                                                                                                                                                | *str*                                                                                                                                                       | :heavy_check_mark:                                                                                                                                          | N/A                                                                                                                                                         |
| `is_enabled`                                                                                                                                                | *bool*                                                                                                                                                      | :heavy_check_mark:                                                                                                                                          | N/A                                                                                                                                                         |
| `timezone`                                                                                                                                                  | *Optional[str]*                                                                                                                                             | :heavy_minus_sign:                                                                                                                                          | N/A                                                                                                                                                         |
| `fixed_timeslot_config`                                                                                                                                     | [Optional[models.V3ServicesNotificationDelayConfigRequestFixedTimeslotConfig]](../../models/v3servicesnotificationdelayconfigrequestfixedtimeslotconfig.md) | :heavy_minus_sign:                                                                                                                                          | N/A                                                                                                                                                         |
| `custom_timeslots_enabled`                                                                                                                                  | *Optional[bool]*                                                                                                                                            | :heavy_minus_sign:                                                                                                                                          | N/A                                                                                                                                                         |
| `custom_timeslots`                                                                                                                                          | [Optional[models.V3ServicesNotificationDelayConfigRequestCustomTimeslots]](../../models/v3servicesnotificationdelayconfigrequestcustomtimeslots.md)         | :heavy_minus_sign:                                                                                                                                          | N/A                                                                                                                                                         |
| `assigned_to`                                                                                                                                               | [Optional[models.V3ServicesNotificationDelayConfigRequestAssignedTo]](../../models/v3servicesnotificationdelayconfigrequestassignedto.md)                   | :heavy_minus_sign:                                                                                                                                          | N/A                                                                                                                                                         |
| `retries`                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                            | :heavy_minus_sign:                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                         |

### Response

**[models.ServicesDelayedNotificationConfigResponse](../../models/servicesdelayednotificationconfigresponse.md)**

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