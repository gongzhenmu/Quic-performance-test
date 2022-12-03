from aioquic.asyncio import serve
if __name__ == "__main__":
    with serve("127.0.0.1",5678) as s:
        pass
