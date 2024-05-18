import binascii
import csv
import json
import os


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
