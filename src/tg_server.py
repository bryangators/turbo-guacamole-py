import asyncio
import websockets
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-p', '--port', type=int, default=8080, help='Port to run the websocket server on.')
    
    args = parser.parse_args()
    
    return args


async def handler(websocket, path):
    print("[SERVER] Client connected")
    await websocket.send("[SERVER] Connected...")
    
    try:
        async for message in websocket:
            print(f"[CLIENT-{websocket.remote_address}]: {message}")
            await websocket.send(f"[SERVER] received: {message}")
    except websockets.exceptions.ConnectionClosed:
        print(f"[SERVER] Client {websocket.remote_address} disconnected")
    except Exception as e:
        print(f"[SERVER] Error: {e}")


async def main():
    # server side cache object will live here or datastore
    cache = {}
    
    args = parse_args()
    
    async with websockets.serve(handler, "", args.port):
        await asyncio.Event().wait()  # run forever
    
if __name__ == "__main__":
    asyncio.run(main())