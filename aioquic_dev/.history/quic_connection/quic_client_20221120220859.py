from aioquic.asyncio.client import connect
from aioquic.quic.configuration import QuicConfiguration
from aioquic.quic.events import QuicEvent, StreamDataReceived

import asyncio
from typing import Optional, cast
import struct


class SimpleSlientProtocol(QuicConfiguration):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pass

    def run(self, data):
        self.send_stream_data(0, data, False)

    def quic_event_received(self, event: QuicEvent) -> None:
        if self._ack_waiter is not None:
            if isinstance(event, StreamDataReceived):
                # parse answer
                length = struct.unpack("!H", bytes(event.data[:2]))[0]
                print(length)

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