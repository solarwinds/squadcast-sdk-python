# Extensions.Msteams

## Overview

### Available Operations

* [create_or_update_config](#create_or_update_config) - Create Or Update MSTeams Configuration

## create_or_update_config

Requires `access_token` as a `Bearer {{token}}` in the `Authorization` header with `user-write` scope.

### Example Usage

<!-- UsageSnippet language="python" operationID="MSTeams_createOrUpdateMsteamsConfiguration" method="post" path="/v3/extensions/msteams/config" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as ss_client:

    res = ss_client.extensions.msteams.create_or_update_config(default_conversation_name="<value>", default_conversation_id="<id>", is_active=False, is_default_active=False, is_custom_channels_active=True, triggers={
        "all_active": False,
        "custom": [],
    }, tenant_id="<id>", from_id="<id>", connected_teams=[
        {
            "team_id": "<id>",
            "team_name": "<value>",
            "channel_configurations": [
                {
                    "squadcast_team_id": "<id>",
                    "squadcast_team_name": "<value>",
                    "is_all_services": True,
                    "services": [
                        {
                            "squadcast_service_id": "<id>",
                            "squadcast_service_name": "<value>",
                        },
                    ],
                    "msteams_channel_id": "<id>",
                    "msteams_channel_name": "<value>",
                },
            ],
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                     | Type                                                                                                                                          | Required                                                                                                                                      | Description                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `default_conversation_name`                                                                                                                   | *str*                                                                                                                                         | :heavy_check_mark:                                                                                                                            | The display name for the default conversation/channel.                                                                                        |
| `default_conversation_id`                                                                                                                     | *str*                                                                                                                                         | :heavy_check_mark:                                                                                                                            | The unique identifier for the default MS Teams conversation/channel.                                                                          |
| `is_active`                                                                                                                                   | *bool*                                                                                                                                        | :heavy_check_mark:                                                                                                                            | A master switch to enable or disable the entire integration.                                                                                  |
| `is_default_active`                                                                                                                           | *bool*                                                                                                                                        | :heavy_check_mark:                                                                                                                            | Determines if notifications should be sent to the default channel.                                                                            |
| `is_custom_channels_active`                                                                                                                   | *bool*                                                                                                                                        | :heavy_check_mark:                                                                                                                            | Determines if notifications should be sent to custom-configured channels.                                                                     |
| `triggers`                                                                                                                                    | [models.V3ExtensionsMSTeamsTriggers](../../models/v3extensionsmsteamstriggers.md)                                                             | :heavy_check_mark:                                                                                                                            | Configuration for which alerts are sent to the MS Teams channel.                                                                              |
| `tenant_id`                                                                                                                                   | *str*                                                                                                                                         | :heavy_check_mark:                                                                                                                            | The Azure AD Tenant ID of the organization that owns this extension.                                                                          |
| `from_id`                                                                                                                                     | *str*                                                                                                                                         | :heavy_check_mark:                                                                                                                            | The Azure AD Object ID of the user who created this extension.                                                                                |
| `connected_teams`                                                                                                                             | List[[models.V3ExtensionsMSTeamsConnectedTeams](../../models/v3extensionsmsteamsconnectedteams.md)]                                           | :heavy_check_mark:                                                                                                                            | A list of all MS Teams (teams) connected to this organization.                                                                                |
| `custom_incident_alert_state`                                                                                                                 | [Optional[models.V3ExtensionsMSTeamsIncidentActionAlertState]](../../models/v3extensionsmsteamsincidentactionalertstate.md)                   | :heavy_minus_sign:                                                                                                                            | A user-friendly way to configure which incident action alerts are active. This is translated by the backend into the 'triggers.custom' array. |
| `id`                                                                                                                                          | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | The MongoDB ObjectID of the extension document. Should be included for updates.                                                               |
| `organization_id`                                                                                                                             | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | The MongoDB ObjectID of the organization this extension belongs to.                                                                           |
| `retries`                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                              | :heavy_minus_sign:                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                           |

### Response

**[models.MSTeamsCreateOrUpdateMsteamsConfigurationResponse](../../models/msteamscreateorupdatemsteamsconfigurationresponse.md)**

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