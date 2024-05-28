from typing import List
import json
import random
import pathlib


def combine_jsonl_files(files: List[str], n: int) -> List[dict]:
    combined_data = []
    for file in files:
        with open(file, "r") as f:
            data = [json.loads(line) for line in f.readlines()]
            if len(data) < n:
                selected_data = data
            else:
                selected_data = random.sample(data, n)
            combined_data.extend(selected_data)
    return combined_data


def combine_from_folder(folder: str, n: int = 10) -> List[dict]:
    """
    Combine all jsonl files in a folder into a single list of dictionaries. (jsonl files are assumed to be in the folder and its subdirectories)

    Args:
        folder (str): the folder to search for jsonl files
        n (int): the number of records to sample from each file

    Returns:
        List[dict]: a list of dictionaries containing the combined data
    """
    files = []
    for path in pathlib.Path(folder).rglob("*.jsonl"):
        files.append(str(path))

    return combine_jsonl_files(files, n)
