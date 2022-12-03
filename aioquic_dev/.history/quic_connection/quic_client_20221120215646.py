from aioquic.asyncio.client import connect
from aioquic.quic.configuration import QuicConfiguration
import asyncio


class SimpleSlientProtocol(QuicConfiguration):
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__
def main( 
    configuration: QuicConfiguration,
    host: str,
    port: int,
):
    async with connect(
        host,
        port,
        configuration=configuration,
        session_ticket_handler=save_session_ticket,
        create_protocol=DnsClientProtocol,
    ) as client:
        client = cast(DnsClientProtocol, client)
        logger.debug("Sending DNS query")
        answer = await client.query(query_name, query_type)
        logger.info("Received DNS answer\n%s" % answer)
if __name__ =="__main__":
    asyncio.run(
        main(
            configuration=QuicConfiguration(is_client=True),
            host="127.0.0.1",
            port=5678,
        )
    )