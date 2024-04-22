import  websocket 
import threading
import time

class TgClient:
    def __init__(self, url):
        self.cache = {}   
        self._connected = False
        self.ws = websocket.WebSocketApp(url,                                         
                                         on_open=self.on_open,
                                         on_message=self.on_message,
                                         on_error=self.on_error,
                                         on_close=self.on_close)
        self.client_thread = threading.Thread(target=self.run)

    def on_message(self, ws, message):
        print(message)

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws, close_status_code, close_msg):
        print(self.format_client_message("Websocket client closed!"))

    def on_open(self, ws):
        self._connected = True

    def run(self):      
        self.ws.run_forever()
    
    def send(self, message):
        if self.ws and self._connected:
            self.ws.send(message)

    def close(self):
        if self.ws:
            self.ws.close()
    
    def isConnected(self):
        return self._connected
    
    def format_client_message(self, message):
        return f"[CLIENT] {message}"
    
    def start(self):
        self.client_thread.start()