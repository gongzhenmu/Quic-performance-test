from aioquic.asyncio.client import connect
from aioquic.quic.configuration import QuicConfiguration
import asyncio

def main( 
    configuration: QuicConfiguration,
    host: str,
    port: int,
):
    pass
if __name__ =="__main__":
    asyncio.run(
    main(
        configuration=QuicConfiguration(is_client=True),
        host="127.0.0.1",
        port=5678,
    )