import asyncio
import websockets
import argparse

class TG_Websocket:
    def __init__(self, port=8080):
        self.port = port
        self.server = None

    async def start(self):
        print(self.formatted_server_message("Starting the server..."))
        async with websockets.serve(self.handler, "", self.port):
            await asyncio.Event().wait()  # run forever
    
    async def handler(self, websocket, path):
        print(self.formatted_server_message("Client Connected..."))
        await websocket.send(self.formatted_server_message("Connected..."))
        
        try:
            async for message in websocket:
                print(f"[CLIENT-{websocket.remote_address}]: {message}")
                await websocket.send(self.formatted_server_message("Recieved " + message))
        except websockets.exceptions.ConnectionClosed:
            print(self.formatted_server_message(f"Client {websocket.remote_address} disconnected"))
        except Exception as e:
            print(self.formatted_server_message(f"Error: {e}"))
            
    def formatted_server_message(self, message):
        return f"[SERVER] {message}"
                
def parse_args():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-p', '--port', type=int, default=8080, help='Port to run the websocket server on.')
    
    args = parser.parse_args()
    
    return args