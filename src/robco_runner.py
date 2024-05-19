from pathlib import Path
import time
from typing import Optional, Tuple, Union
from fmeval.model_runners.model_runner import ModelRunner
import json
import websocket


class RobcoRunner(ModelRunner):
    def __init__(self, ws_address: str, *args, **kwargs):
        assert ws_address is not None, "WebSocket address must be provided"
        self.ws_address = ws_address
        self.ws = None
        self.connect()

    def connect(self):
        conn = websocket.create_connection(self.ws_address, timeout=60)
        self.ws = conn

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["ws"]
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self.connect()

    def predict(self, prompt: str) -> Tuple[Optional[str], Optional[float]]:
        request_params = {
            "message": prompt,
        }
        request_json = json.dumps(request_params)

        try:
            # Send the request
            self.ws.send(request_json)
            # Receive the response
            response_json = self.ws.recv()
            # Convert the JSON string to a dictionary
            response_dict = json.loads(response_json)
            # Extract the result from the response dictionary
            result = response_dict.get("message")
            return result, None
        except websocket.WebSocketTimeoutException:
            print("WebSocket timeout, retrying...")
            time.sleep(5)  # Wait before retrying
            self.connect()  # Reconnect the WebSocket
            try:
                self.ws.send(request_json)
                response_json = self.ws.recv()
                response_dict = json.loads(response_json)
                result = response_dict.get("message")
                return result, None
            except Exception as e:
                print(f"Failed after retry: {e}")
                return None, None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None, None
