# V3AuthAccessTokenData

Access token response returned by the OAuth endpoint.


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `access_token`                                               | *str*                                                        | :heavy_check_mark:                                           | JWT access token used as Bearer token for API requests.      |
| `expires_at`                                                 | *int*                                                        | :heavy_check_mark:                                           | Unix timestamp when the access token expires.                |
| `issued_at`                                                  | *int*                                                        | :heavy_check_mark:                                           | Unix timestamp when the access token was issued.             |
| `refresh_token`                                              | *str*                                                        | :heavy_check_mark:                                           | Refresh token that can be used to obtain a new access token. |
| `type`                                                       | *str*                                                        | :heavy_check_mark:                                           | Token type, e.g. "Bearer".                                   |