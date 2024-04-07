import pytest
from src.tg_client import TgClient
from src.tg_websocket import TgServer
import time

@pytest.fixture
async def websocket_server():
    print("start...........aflk;a;jdf;alkdjfa;lkj")
    server = TgServer(8080)
    print("HELLLLLLLLLLLLOOOOOOOOOOOOOOOOOOOOOOOO")
    await server.start()
    yield server

@pytest.mark.asyncio
async def test_connection(websocket_server):
    print(websocket_server)
    print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
    client = TgClient("ws://localhost:8080")
    client.start()
    time.sleep(1)
    
    
    client.close()

