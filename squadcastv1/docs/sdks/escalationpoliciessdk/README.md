# EscalationPolicies

## Overview

### Available Operations

* [get_by_team](#get_by_team) - Get Escalation Policy By team
* [create](#create) - Create Escalation Policies
* [remove](#remove) - Remove Escalation Policy
* [get_by_id](#get_by_id) - Get Escalation Policy By ID
* [update](#update) - Update Escalation Policy

## get_by_team

Returns all escalation policy details of the given `ownerID` (teamId) in the request param.
Requires `access_token` as a `Bearer {{token}}` in the `Authorization` header with `read` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="EscalationPolicies_getEscalationPolicyByTeam" method="get" path="/v3/escalation-policies" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.escalation_policies.get_by_team(owner_id="<id>")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                       | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `owner_id`                                                                                                      | *str*                                                                                                           | :heavy_check_mark:                                                                                              | here owner_id represents team_id, if  team_id is not provided, it will return escalation policies of all teams. |
| `page_number`                                                                                                   | *Optional[int]*                                                                                                 | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |
| `page_size`                                                                                                     | *Optional[int]*                                                                                                 | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |
| `retries`                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                | :heavy_minus_sign:                                                                                              | Configuration to override the default retry behavior of the client.                                             |

### Response

**[models.EscalationPoliciesGetEscalationPolicyByTeamResponse](../../models/escalationpoliciesgetescalationpolicybyteamresponse.md)**

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

Add escalation policy to the organization. Returns the escalation policy object in response.
Requires `access_token` as a `Bearer {{token}}` in the `Authorization` header with `user-write` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="EscalationPolicies_createEscalationPolicies" method="post" path="/v3/escalation-policies" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.escalation_policies.create(owner_id="<id>", name="<value>", description="properly aw gerbil address co-producer guzzle delight difficult", repetition=549305, repeat_after=226311, rules=[
        {
            "escalation_time": 646220,
            "via": [
                "<value 1>",
                "<value 2>",
            ],
            "roundrobin_enabled": True,
            "roundrobin_next_index": 685302,
            "entities": [],
            "escalate_within_roundrobin": True,
            "repetition": 149319,
            "repeat_after": 619552,
        },
    ], enable_incident_reminders=False, incident_reminder_rules=[], enable_incident_retrigger=False, retrigger_after=660610)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                         | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `owner_id`                                                                                                        | *str*                                                                                                             | :heavy_check_mark:                                                                                                | The ID of the team that owns this escalation policy.                                                              |
| `name`                                                                                                            | *str*                                                                                                             | :heavy_check_mark:                                                                                                | The name of the escalation policy.                                                                                |
| `description`                                                                                                     | *str*                                                                                                             | :heavy_check_mark:                                                                                                | A description of the escalation policy.                                                                           |
| `repetition`                                                                                                      | *int*                                                                                                             | :heavy_check_mark:                                                                                                | The number of times the entire policy should be repeated.                                                         |
| `repeat_after`                                                                                                    | *int*                                                                                                             | :heavy_check_mark:                                                                                                | The time in minutes after which the policy should be repeated.                                                    |
| `rules`                                                                                                           | List[[models.V3EscalationPoliciesEscalationPolicyRule](../../models/v3escalationpoliciesescalationpolicyrule.md)] | :heavy_check_mark:                                                                                                | The rules that define the escalation steps.                                                                       |
| `enable_incident_reminders`                                                                                       | *bool*                                                                                                            | :heavy_check_mark:                                                                                                | Enable or disable incident reminders.                                                                             |
| `incident_reminder_rules`                                                                                         | List[[models.V3EscalationPoliciesIncidentReminderRule](../../models/v3escalationpoliciesincidentreminderrule.md)] | :heavy_check_mark:                                                                                                | The rules for incident reminders.                                                                                 |
| `enable_incident_retrigger`                                                                                       | *bool*                                                                                                            | :heavy_check_mark:                                                                                                | Enable or disable automatic incident re-triggering.                                                               |
| `retrigger_after`                                                                                                 | *int*                                                                                                             | :heavy_check_mark:                                                                                                | The time in hours after which an incident should be re-triggered.                                                 |
| `entity_owner`                                                                                                    | [Optional[models.CommonV3EntityOwner]](../../models/commonv3entityowner.md)                                       | :heavy_minus_sign:                                                                                                | The owner of the entity.                                                                                          |
| `retries`                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                  | :heavy_minus_sign:                                                                                                | Configuration to override the default retry behavior of the client.                                               |

### Response

**[models.EscalationPoliciesCreateEscalationPoliciesResponse](../../models/escalationpoliciescreateescalationpoliciesresponse.md)**

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

Remove escalation policy from the organization. Upon success, the escalation policy will be removed from the organization.
Requires `access_token` as a `Bearer {{token}}` in the `Authorization` header with `user-write` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="EscalationPolicies_removeEscalationPolicy" method="delete" path="/v3/escalation-policies/{escalationPolicyID}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.escalation_policies.remove(escalation_policy_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `escalation_policy_id`                                              | *str*                                                               | :heavy_check_mark:                                                  | (Required) escalation policy ID                                     |
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

Returns an escalation policy details of the given `escalationPolicyID` in the request param.
Requires `access_token` as a `Bearer {{token}}` in the `Authorization` header with `read` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="EscalationPolicies_getEscalationPolicyById" method="get" path="/v3/escalation-policies/{escalationPolicyID}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.escalation_policies.get_by_id(escalation_policy_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `escalation_policy_id`                                              | *str*                                                               | :heavy_check_mark:                                                  | (Required) escalation policy ID                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.EscalationPoliciesGetEscalationPolicyByIDResponse](../../models/escalationpoliciesgetescalationpolicybyidresponse.md)**

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

Update organization escalation policy details.
Requires `access_token` as a `Bearer {{token}}` in the `Authorization` header with `user-write` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="EscalationPolicies_updateEscalationPolicy" method="post" path="/v3/escalation-policies/{escalationPolicyID}" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.escalation_policies.update(escalation_policy_id="<id>", v3_escalation_policies_update_escalation_policy_request=open("example.file", "rb"))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `escalation_policy_id`                                              | *str*                                                               | :heavy_check_mark:                                                  | (Required) escalation policy ID                                     |
| `v3_escalation_policies_update_escalation_policy_request`           | *Union[bytes, IO[bytes], io.BufferedReader]*                        | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.EscalationPoliciesUpdateEscalationPolicyResponse](../../models/escalationpoliciesupdateescalationpolicyresponse.md)**

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