# Workflows

## Overview

### Available Operations

* [list](#list) - List Workflows
* [create](#create) - Create Workflow
* [bulk_enable_disable](#bulk_enable_disable) - Bulk Enable/Disable Workflows
* [delete](#delete) - Delete Workflow
* [get_by_id](#get_by_id) - Get Workflow By ID
* [update](#update) - Update Workflow
* [update_actions_order](#update_actions_order) - Update Actions Order
* [delete_action](#delete_action) - Delete Workflow Action
* [update_action](#update_action) - Update Workflow Action
* [enable_disable](#enable_disable) - Enable/Disable Workflow

## list

Get a list of all Workflows

### Example Usage

<!-- UsageSnippet language="python" operationID="Workflows_listWorkflows" method="get" path="/v3/workflows" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.workflows.list(owner_id="<id>")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `owner_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `page_number`                                                       | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `search`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `event`                                                             | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `actions`                                                           | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `tags`                                                              | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `owner`                                                             | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `created_by`                                                        | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `updated_by`                                                        | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `enabled`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.WorkflowsListWorkflowsResponse](../../models/workflowslistworkflowsresponse.md)**

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

Create a Workflow

### Example Usage

<!-- UsageSnippet language="python" operationID="Workflows_createWorkflow" method="post" path="/v3/workflows" -->
```python
from squadcast_sdk import SquadcastSDK, models


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.workflows.create(title="<value>", owner_id="<id>", trigger="incident_acknowledged", filters=models.V3WorkflowsCreateWorkflowFilter(), actions=[
        {
            "name": "sq_trigger_manual_webhook",
            "data": {
                "id": "<id>",
            },
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                               | Type                                                                                                                    | Required                                                                                                                | Description                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `title`                                                                                                                 | *str*                                                                                                                   | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `owner_id`                                                                                                              | *str*                                                                                                                   | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `trigger`                                                                                                               | [models.V3WorkflowsWorkflowTrigger](../../models/v3workflowsworkflowtrigger.md)                                         | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `filters`                                                                                                               | [models.V3WorkflowsCreateWorkflowFilter](../../models/v3workflowscreateworkflowfilter.md)                               | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `actions`                                                                                                               | List[[models.V3WorkflowsActionRequest](../../models/v3workflowsactionrequest.md)]                                       | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `description`                                                                                                           | *Optional[str]*                                                                                                         | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `owner_type`                                                                                                            | [Optional[models.V3WorkflowsCreateWorkflowRequestOwnerType]](../../models/v3workflowscreateworkflowrequestownertype.md) | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `entity_owner`                                                                                                          | [Optional[models.V3WorkflowsEntityOwner]](../../models/v3workflowsentityowner.md)                                       | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `tags`                                                                                                                  | List[[models.V3WorkflowsTag](../../models/v3workflowstag.md)]                                                           | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `enabled`                                                                                                               | *Optional[bool]*                                                                                                        | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `retries`                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                        | :heavy_minus_sign:                                                                                                      | Configuration to override the default retry behavior of the client.                                                     |

### Response

**[models.WorkflowsCreateWorkflowResponse](../../models/workflowscreateworkflowresponse.md)**

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

## bulk_enable_disable

Bulk enable or disable workflows

### Example Usage

<!-- UsageSnippet language="python" operationID="Workflows_bulkEnabledisableWorkflows" method="put" path="/v3/workflows/enable" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.workflows.bulk_enable_disable(owner_id="<id>", enabled=False, workflow_ids=[
        124939,
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `owner_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `enabled`                                                           | *bool*                                                              | :heavy_check_mark:                                                  | N/A                                                                 |
| `workflow_ids`                                                      | List[*int*]                                                         | :heavy_check_mark:                                                  | N/A                                                                 |
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

## delete

Delete a workflow by ID

### Example Usage

<!-- UsageSnippet language="python" operationID="Workflows_deleteWorkflow" method="delete" path="/v3/workflows/{workflowID}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.workflows.delete(workflow_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `workflow_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
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

Get a workflow by ID

### Example Usage

<!-- UsageSnippet language="python" operationID="Workflows_getWorkflowById" method="get" path="/v3/workflows/{workflowID}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.workflows.get_by_id(workflow_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `workflow_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.V3WorkflowsGetWorkflowByIDResponse](../../models/v3workflowsgetworkflowbyidresponse.md)**

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

Update a Workflow

### Example Usage

<!-- UsageSnippet language="python" operationID="Workflows_updateWorkflow" method="patch" path="/v3/workflows/{workflowID}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.workflows.update(workflow_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                           | Type                                                                                                                                | Required                                                                                                                            | Description                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `workflow_id`                                                                                                                       | *str*                                                                                                                               | :heavy_check_mark:                                                                                                                  | N/A                                                                                                                                 |
| `title`                                                                                                                             | *Optional[str]*                                                                                                                     | :heavy_minus_sign:                                                                                                                  | N/A                                                                                                                                 |
| `description`                                                                                                                       | *Optional[str]*                                                                                                                     | :heavy_minus_sign:                                                                                                                  | N/A                                                                                                                                 |
| `owner_id`                                                                                                                          | *Optional[str]*                                                                                                                     | :heavy_minus_sign:                                                                                                                  | N/A                                                                                                                                 |
| `owner_type`                                                                                                                        | [Optional[models.V3WorkflowsCreateWorkflowRequestUpdateOwnerType]](../../models/v3workflowscreateworkflowrequestupdateownertype.md) | :heavy_minus_sign:                                                                                                                  | N/A                                                                                                                                 |
| `entity_owner`                                                                                                                      | [Optional[models.V3WorkflowsEntityOwnerUpdate]](../../models/v3workflowsentityownerupdate.md)                                       | :heavy_minus_sign:                                                                                                                  | N/A                                                                                                                                 |
| `tags`                                                                                                                              | List[[models.V3WorkflowsTag](../../models/v3workflowstag.md)]                                                                       | :heavy_minus_sign:                                                                                                                  | N/A                                                                                                                                 |
| `trigger`                                                                                                                           | [Optional[models.V3WorkflowsWorkflowTrigger]](../../models/v3workflowsworkflowtrigger.md)                                           | :heavy_minus_sign:                                                                                                                  | N/A                                                                                                                                 |
| `filters`                                                                                                                           | [Optional[models.V3WorkflowsCreateWorkflowFilter]](../../models/v3workflowscreateworkflowfilter.md)                                 | :heavy_minus_sign:                                                                                                                  | N/A                                                                                                                                 |
| `actions`                                                                                                                           | List[[models.V3WorkflowsActionRequest](../../models/v3workflowsactionrequest.md)]                                                   | :heavy_minus_sign:                                                                                                                  | N/A                                                                                                                                 |
| `enabled`                                                                                                                           | *Optional[bool]*                                                                                                                    | :heavy_minus_sign:                                                                                                                  | N/A                                                                                                                                 |
| `retries`                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                    | :heavy_minus_sign:                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                 |

### Response

**[models.WorkflowsUpdateWorkflowResponse](../../models/workflowsupdateworkflowresponse.md)**

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

## update_actions_order

Update action order in a workflow

### Example Usage

<!-- UsageSnippet language="python" operationID="Workflows_updateActionsOrder" method="patch" path="/v3/workflows/{workflowID}/actions/reorder" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.workflows.update_actions_order(workflow_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `workflow_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `action_order`                                                      | List[*int*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.V3WorkflowsUpdateActionsOrderResponse](../../models/v3workflowsupdateactionsorderresponse.md)**

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

## delete_action

Delete an action by action ID

### Example Usage

<!-- UsageSnippet language="python" operationID="Workflows_deleteWorkflowAction" method="delete" path="/v3/workflows/{workflowID}/actions/{actionID}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.workflows.delete_action(workflow_id="<id>", action_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `workflow_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `action_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
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

## update_action

Update an action by action ID

### Example Usage

<!-- UsageSnippet language="python" operationID="Workflows_updateWorkflowAction" method="patch" path="/v3/workflows/{workflowID}/actions/{actionID}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.workflows.update_action(workflow_id="<id>", action_id="<id>", v3_workflows_action_request_update={
        "name": "slack_message_channel",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `workflow_id`                                                                           | *str*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `action_id`                                                                             | *str*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `v3_workflows_action_request_update`                                                    | [models.V3WorkflowsActionRequestUpdate](../../models/v3workflowsactionrequestupdate.md) | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.V3WorkflowsActionResponse](../../models/v3workflowsactionresponse.md)**

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

## enable_disable

Enable or disable workflow by ID

### Example Usage

<!-- UsageSnippet language="python" operationID="Workflows_enabledisableWorkflow" method="patch" path="/v3/workflows/{workflowID}/enable" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.workflows.enable_disable(workflow_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `workflow_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `enabled`                                                           | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
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