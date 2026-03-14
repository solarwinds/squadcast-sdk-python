# Auth

## Overview

### Available Operations

* [auth_get_access_token](#auth_get_access_token) - Get Access Token

## auth_get_access_token

Get access token to make authenticated HTTP requests to the Squadcast API.
Send your refresh token (obtained from the Squadcast web application) in the
`X-Refresh-Token` header.

### Example Usage

<!-- UsageSnippet language="python" operationID="Auth_getAccessToken" method="get" path="/oauth/access-token" -->
```python
from squadcast_sdk import SquadcastSDK


with SquadcastSDK() as ss_client:

    res = ss_client.auth.auth_get_access_token(x_refresh_token="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `x_refresh_token`                                                           | *str*                                                                       | :heavy_check_mark:                                                          | (Required) Send your refresh token obtained from Squadcast web application. |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |
| `server_url`                                                                | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | An optional server URL to use.                                              |

### Response

**[models.AuthGetAccessTokenResponse](../../models/authgetaccesstokenresponse.md)**

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