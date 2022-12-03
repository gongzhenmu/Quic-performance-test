from aioquic.asyncio.client import connect
from aioquic.quic.configuration import QuicConfiguration
import asyncio
from typing import Optional, cast


class SimpleSlientProtocol(QuicConfiguration):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pass

    
async def main( 
    configuration: QuicConfiguration,
    host: str,
    port: int,
):
    async with connect(
        host,
        port,
        configuration=configuration,
        create_protocol=SimpleSlientProtocol,
    ) as client:
        client = cast(SimpleSlientProtocol, client)
        answer = await client.query(query_name, query_type)
if __name__ =="__main__":
    asyncio.run(
        main(
            configuration=QuicConfiguration(is_client=True),
            host="127.0.0.1",
            port=5678,
        )
    )