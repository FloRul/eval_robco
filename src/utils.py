import binascii
import csv
import json
import os
import logging
import json
import random
import pathlib
import random
from typing import List, Generator
from websockets.sync.client import connect


def csv_to_jsonl(csv_file_path: str, jsonl_file_path: str):
    with open(csv_file_path, "r", encoding="utf8") as csv_file:
        reader = csv.DictReader(csv_file, delimiter=";")
        data = list(reader)

    with open(jsonl_file_path, "w", encoding="utf8") as jsonl_file:
        for row in data:
            json.dump(row, jsonl_file)
            jsonl_file.write("\n")


def jsonl_to_csv(jsonl_file_path: str, csv_file_path: str):
    with open(jsonl_file_path, "r", encoding="utf8") as jsonl_file:
        data = [json.loads(line) for line in jsonl_file]

    with open(csv_file_path, "w", encoding="utf8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=data[0].keys(), delimiter=";")
        writer.writeheader()
        writer.writerows(data)


def get_salt():
    # Generate a salt of 16 bytes
    salt = os.urandom(4)
    return binascii.hexlify(salt).decode()


import queue
import threading
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def combine_jsonl_files(files: List[str], n: int) -> Generator[str, None, None]:
    for file in files:
        with open(file, "r", encoding="utf8") as f:
            data = f.readlines()
            if len(data) < n:
                selected_data = data
            else:
                selected_data = random.sample(data, n)
            yield from selected_data


def combine_from_folder(folder: str, n: int = 10) -> Generator[str, None, None]:
    """
    Combine all jsonl files in a folder into a generator of strings. (jsonl files are assumed to be in the folder and its subdirectories)

    Args:
        folder (str): the folder to search for jsonl files
        n (int): the number of records to sample from each file

    Yields:
        str: a string representing a single jsonl line from the combined data
    """
    files = [str(path) for path in pathlib.Path(folder).rglob("*.jsonl")]
    yield from combine_jsonl_files(files, n)


class ThrottledWebSocket:
    def __init__(self, ws: str):
        self.ws = connect(ws)
        self.queue = queue.Queue()
        self.thread = threading.Thread(target=self._send_loop)
        self.thread.daemon = True
        self.thread.start()

    def send(self, message):
        self.queue.put(message)

    def recv(self):
        return self.ws.recv()

    def _send_loop(self):
        while True:
            message = self.queue.get()
            try:
                self.ws.send(message)
                logger.info(f"Message sent: {message}")
                time.sleep(float(os.environ.get("WS_THROTTLE")))  # throttle rate
            except Exception as e:
                logger.error(f"Error sending message: {e}")
