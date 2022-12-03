from aioquic.asyncio.client import connect


if __name__ =="__main__":
    with connect("www.google.com", 443) as conn:
        conn.send(b"GET / HTTP/1.1\r")

    # with connect(
    #         host,
    #         port,
    #         configuration=configuration,
    #         session_ticket_handler=save_session_ticket,
    #         create_protocol=DnsClientProtocol,
    #     ) as client:
    #         client = cast(DnsClientProtocol, client)
    #         logger.debug("Sending DNS query")
    #         answer = await client.query(query_name, query_type)
    #         logger.info("Received DNS answer\n%s" % answer)