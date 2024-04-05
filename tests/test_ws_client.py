import pytest
from src.tg_client import TgClient
from src.tg_server import main
import time

@pytest.fixture
def websocket_client():
    time.sleep(1)  # Give the server some time to start
    client = TgClient("ws://localhost:8080") 
    client.start()
    yield client  
    
    client.close()

# As of right now the server needs to be running for this to work...
# TODO - setup a mock ws server for the client to use
def test_connection(websocket_client):
    time.sleep(2)
    assert websocket_client.isConnected()
