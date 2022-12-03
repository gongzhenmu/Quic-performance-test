from aioquic.asyncio import server
if __name__ == "__main__":
    with server("127.0.0.1",5678) as s:
        