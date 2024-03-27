import asyncio
import websockets

class WebSocketClient:
    """Client with in memory cache that will send/receive messages from websocket server
    """
    def __init__(self, url:str="ws://localhost:8000"):
        """_summary_

        Args:
            url (_type_, optional): _description_. Defaults to "ws://localhost:8000".
        """
        self.url = url
        self.websocket = None

    async def connect(self):
        """connects to server
        """
        self.websocket = await websockets.connect(self.url)

    async def send_message(self, message: str):
        """async method to send a message to server

        Args:
            message (str): message sent to server

        Raises:
            Exception: if connection is not established
        """
        if self.websocket:
            await self.websocket.send(message)
        else:
            raise Exception("WebSocket connection is not established")

    async def receive_message(self) -> str:
        """async method returns any message received from server

        Raises:
            Exception: _description_

        Returns:
            str: message received
        """
        if self.websocket:
            return await self.websocket.recv()
        else:
            raise Exception("WebSocket connection is not established")

    async def close(self):
        """closes connection to websocket server
        """
        if self.websocket:
            await self.websocket.close()

    async def run(self):
        """ run client indefinitely and asynchronously send/receive messages from server
        """
        await self.connect()

        try:
            while True:
                # Send message
                message_to_send = input("Type a message to send (or 'exit' to quit): ")
                if message_to_send.lower() == 'exit':
                    break
                await self.send_message(message_to_send)

                # Receive message
                received_message = await self.receive_message()
                print(received_message)
        finally:
            await self.close()

# Example usage:
asyncio.run(WebSocketClient().run())
