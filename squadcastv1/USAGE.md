<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from squadcast_sdk import SquadcastSDK


with SquadcastSDK() as ss_client:

    res = ss_client.auth.auth_get_access_token(x_refresh_token="<value>")

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from squadcast_sdk import SquadcastSDK

async def main():

    async with SquadcastSDK() as ss_client:

        res = await ss_client.auth.auth_get_access_token_async(x_refresh_token="<value>")

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->