from aioquic.asyncio import client
from aioquic.quic.configuration import QuicConfiguration
from aioquic.quic.events import QuicEvent, StreamDataReceived

import asyncio
from typing import Optional, cast
import struct

import aioquic 
class QUIC_client(client):
    def __init__(self, host, port,):
        super().__init__(host, port)
        pass

    async def run(self, data):
        async with aioquic.asyncio.connect(host=self.host, port=self.port, configuration=self.config) as client:
            await client.wait_connected()
            reader, writer = await client.create_stream()
            for i in range(300):
                writer.write(b'123123123')
                writer.write(b'PAUSE\n')
            client.transmit()
            line = await reader.readline()
            print(line)
            client.close()
            await client.wait_closed()
    def quic_event_received(self, event: QuicEvent) -> None:
        if self._ack_waiter is not None:
            if isinstance(event, StreamDataReceived):
                # parse answer
                length = struct.unpack("!H", bytes(event.data[:2]))[0]
                print(length)


if __name__ =="__main__":
    asyncio.run(
        main(
            configuration=QuicConfiguration(is_client=True),
            host="127.0.0.1",
            port=5678,
        )
    )