from tg_websocket import TG_Websocket
from fastapi import FastAPI, WebSocket, WebSocketDisconnect 
from contextlib import asynccontextmanager
import asyncio

#create server instance
server = TG_Websocket(port=8080)

#construct/destruct code for the server
@asynccontextmanager
async def lifespan(app: FastAPI):
    asyncio.create_task(server.start())
    yield
    # Clean up the server here
  
#fast api instance  
app = FastAPI(lifespan=lifespan)

#setup endpoints
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    async for message in websocket:
        await server.handler(websocket, message)  # Delegate handling to the server
