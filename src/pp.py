from utils import csv_to_jsonl, jsonl_to_csv


def main():
    csv_to_jsonl("src/misc/faq.csv", "src/misc/faq.jsonl")


if __name__ == "__main__":
    main()
