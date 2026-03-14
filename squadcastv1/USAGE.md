<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from squadcast import SquadcastSDK


with SquadcastSDK() as squadcast_sdk:

    res = squadcast_sdk.auth.auth_get_access_token(x_refresh_token="<value>")

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from squadcast import SquadcastSDK

async def main():

    async with SquadcastSDK() as squadcast_sdk:

        res = await squadcast_sdk.auth.auth_get_access_token_async(x_refresh_token="<value>")

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->