from aioquic.asyncio import server,client

import asyncio as asc
import aioquic.asyncio
from aioquic.quic.configuration import QuicConfiguration
import ssl

class QUIC_client(client):
    def __init__(self, host, port, use_json):
        super().__init__(host, port, use_json)
        self.traffic_type = 'quic'
        self.payload = b'p'*(self.quic_payload_size-1)+b'\n'
        self.config = QuicConfiguration(
            is_client = True,
            verify_mode = ssl.CERT_NONE
            )

    async def _maintask(self, time):
        self._infomessage(f'connecting to server {self.host}:{self.port}')
        async with aioquic.asyncio.connect(host=self.host, port=self.port, configuration=self.config) as client:
            await client.wait_connected()
            self._infomessage(message=f'connection successful')
            reader, writer = await client.create_stream()
            self._infomessage(message=f'stream created, now transmitting')

            timetofinish = millis() + (time*1000)
            while(millis() < timetofinish):
                for i in range(300):
                    writer.write(self.payload)
                writer.write(b'PAUSE\n')
                client.transmit()
                #HERE
                #when i just send data over and over again program hangs on client side
                #thats why i send 'PAUSE' and wait for 'CONTINUE'
                #its just a temporary solution but i couldnt find anything to just wait until send is complete
                line = await reader.readline()
                if line == b'CONTINUE\n':
                    #self._infomessage(message=f'continuing...')
                    pass
                else:
                    self._infomessage(message=f'connection closed')
                    break

            writer.write(b'STOP\n')
            client.transmit()
            client.close()
            await client.wait_closed()
            self._infomessage(message=f'client finished')

    def run_test(self, time):
        super().run_test(time)
        loop = asc.get_event_loop()
        loop.run_until_complete(self._maintask(time))



class QUIC_server(server):
    def __init__(self, port, interval, use_json):
        super().__init__(port, interval, use_json)
        self.traffic_type = 'quic'
        self.config = QuicConfiguration(
            is_client = False
            )
        self.config.load_cert_chain('cert.pem', 'key.pem')
        self.loop = asc.get_event_loop()

    def _streamhandler(self, reader, writer):
        self._infomessage(message='stream created')
        self.currentstreamtask = self.loop.create_task(self._currentstreamhandler(reader, writer))

    async def _currentstreamhandler(self, reader, writer):
        data_counter = 0
        timer = millis()
        while(True):
            line = await reader.readline()
            if line == b'':
                self._infomessage(message='connection interrupted! now exitting', is_error=True)
                return
            elif line == b'STOP\n':
                self._infomessage('server finished')
                self.loop.stop()
                return
            elif line == b'PAUSE\n':
                    writer.write(b'CONTINUE\n')
                    #TODO find a better way to control data flow
            else:
                data_counter += 1
                if (millis() - timer) > (self.interval*1000):
                    timer = millis()
                    self._datamessage(bps_value=(data_counter*self.quic_payload_size*8/self.interval))
                    data_counter = 0

    def listen(self):
        super().listen()
        try:
            self.server_task = self.loop.create_task(
                aioquic.asyncio.serve(host='0.0.0.0',
                port=self.port,
                configuration=self.config,
                stream_handler=self._streamhandler
                ))
            self.loop.run_forever()
        except asc.CancelledError:
            print('cancelled error')

#basically when running a test
#QUIC_client or QUIC_server instance is created
#and then run_test() or listen() is called

if __name__ =="__main__":
