from aioquic.asyncio import client
# from aioquic.quic.configuration import QuicConfiguration
# from aioquic.quic.events import QuicEvent, StreamDataReceived

import asyncio
from typing import Optional, cast
import struct

import aioquic 
class QUIC_client(client):
    def __init__(self, host, port,use_json):
        super().__init__(host, port,use_json)
        pass

    # async def run(self, data):
    #     async with aioquic.asyncio.connect(host=self.host, port=self.port, configuration=self.config) as client:
    #         await client.wait_connected()
    #         reader, writer = await client.create_stream()
    #         for i in range(300):
    #             writer.write(b'123123123')
    #             writer.write(b'PAUSE\n')
    #         client.transmit()
    #         line = await reader.readline()
    #         print(line)
    #         client.close()
    #         await client.wait_closed()
  

if __name__ =="__main__":
    a = QUIC_client("127.0.0.1", 5678,True)
    # a.run(b"21234234")