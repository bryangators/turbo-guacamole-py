from src.tg_client import TgClient
import time

if __name__ == "__main__":
    # example setup for client websocket
    client = TgClient("ws://localhost:8080")
    client.start()
    
    #wait for websocket to connect
    # TODO: need a better handling of connection handling 
    print(client.format_client_message("Connecting to server..."))
    time.sleep(3)
    
    if not client.isConnected():
        print(client.format_client_message("Something went wrong..."))
        exit(1)
    
    client.send("*********sending a test to the server*******")