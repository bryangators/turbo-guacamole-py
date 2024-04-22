from src.tg_client import TgClient
import time

if __name__ == "__main__":
    try:
        # Example setup for client websocket
        client = TgClient("ws://localhost:8080")
        client.start()
        
        # Wait for websocket to connect
        # TODO: need a better handling of connection handling 
        print(client.format_client_message("Connecting to server..."))
        time.sleep(1)
        
        if not client.isConnected():
            print(client.format_client_message("Something went wrong..."))
            exit(1)
        
        ## LOGIC FOR APPLIACTION CAN BE RUN HERE
        client.send("*********sending a test to the server*******")
        
        while True:
            # Add some work here if needed
            pass
        
    except KeyboardInterrupt:
        client.close()
