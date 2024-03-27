import asyncio
import websockets
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-p', '--port', type=int, default=8000, help='Port to run the websocket server on.')
    
    args = parser.parse_args()
    
    return args


async def handler(websocket, path):
    print(f"Client connected")

    while True:
        message = await websocket.recv()
        
        print(f"Received: {message}")
        
        await websocket.send(f"Server received: {message}")


async def main():
    # server side cache object will live here or datastore
    cache = {}
    
    args = parse_args()
    
    async with websockets.serve(handler, "", args.port):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())