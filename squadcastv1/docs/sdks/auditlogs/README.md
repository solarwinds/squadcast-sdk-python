# AuditLogs

## Overview

### Available Operations

* [list](#list) - List all Audit Logs
* [export](#export) - Initiate an asynchronous export of audit logs based on the provided filters. The export file will be generated and available for download. Use 'Get details of Audit Logs export history by ID' API to retrieve the download URL.
* [list_export_history](#list_export_history) - List all Audit Logs export history
* [get_export_history_by_id](#get_export_history_by_id) - Get details of Audit Logs export history by ID
* [get_by_id](#get_by_id) - Get audit log by ID

## list

List all Audit Logs
Returns array of audit logs for given team and filters

### Example Usage

<!-- UsageSnippet language="python" operationID="AuditLogs_listAuditLogs" method="get" path="/v3/audit-logs" -->
```python
from datetime import date
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.audit_logs.list(page_size=832442, page_number=555332, start_date=date.fromisoformat("2023-03-04"), end_date=date.fromisoformat("2024-08-07"))

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `page_size`                                                                  | *int*                                                                        | :heavy_check_mark:                                                           | N/A                                                                          |
| `page_number`                                                                | *int*                                                                        | :heavy_check_mark:                                                           | N/A                                                                          |
| `start_date`                                                                 | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects) | :heavy_check_mark:                                                           | N/A                                                                          |
| `end_date`                                                                   | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects) | :heavy_check_mark:                                                           | N/A                                                                          |
| `action`                                                                     | List[*str*]                                                                  | :heavy_minus_sign:                                                           | N/A                                                                          |
| `resource`                                                                   | List[*str*]                                                                  | :heavy_minus_sign:                                                           | N/A                                                                          |
| `actor`                                                                      | List[*str*]                                                                  | :heavy_minus_sign:                                                           | N/A                                                                          |
| `team`                                                                       | List[*str*]                                                                  | :heavy_minus_sign:                                                           | N/A                                                                          |
| `client`                                                                     | List[[models.Client](../../models/client.md)]                                | :heavy_minus_sign:                                                           | N/A                                                                          |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[models.AuditLogsListAuditLogsResponse](../../models/auditlogslistauditlogsresponse.md)**

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

## export

Export Audit logs
Initiates export of audit logs based on provided filters

### Example Usage

<!-- UsageSnippet language="python" operationID="AuditLogs_exportAuditLogs" method="post" path="/v3/audit-logs/export" -->
```python
from datetime import date
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.audit_logs.export(filters={
        "start_date": date.fromisoformat("2025-07-29"),
        "end_date": date.fromisoformat("2023-09-09"),
    }, name="<value>", export_type="json")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `filters`                                                           | [models.Filters](../../models/filters.md)                           | :heavy_check_mark:                                                  | N/A                                                                 |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `export_type`                                                       | [models.ExportType](../../models/exporttype.md)                     | :heavy_check_mark:                                                  | N/A                                                                 |
| `description`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.V3AuditLogsExportAuditLogsResponse](../../models/v3auditlogsexportauditlogsresponse.md)**

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

## list_export_history

List all Audit Logs export history
Returns array of audit logs export history

### Example Usage

<!-- UsageSnippet language="python" operationID="AuditLogs_listAuditLogsExportHistory" method="get" path="/v3/audit-logs/export/history" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.audit_logs.list_export_history(page_size=159672, page_number=351281)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `page_size`                                                         | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `page_number`                                                       | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AuditLogsListAuditLogsExportHistoryResponse](../../models/auditlogslistauditlogsexporthistoryresponse.md)**

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

## get_export_history_by_id

Get details of Audit Logs export history by ID
Returns audit log export history details for the specified ID

### Example Usage

<!-- UsageSnippet language="python" operationID="AuditLogs_getAuditLogsExportHistoryById" method="get" path="/v3/audit-logs/export/history/{id}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.audit_logs.get_export_history_by_id(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.V3AuditLogsGetAuditLogExportHistoryByIDResponse](../../models/v3auditlogsgetauditlogexporthistorybyidresponse.md)**

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

Get audit log by ID
Returns audit log details for the specified ID

### Example Usage

<!-- UsageSnippet language="python" operationID="AuditLogs_getAuditLogById" method="get" path="/v3/audit-logs/{id}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.audit_logs.get_by_id(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.V3AuditLogsGetAuditLogByIDResponse](../../models/v3auditlogsgetauditlogbyidresponse.md)**

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