import csv
import json
import os

SOURCE_TEXT = "sample_input.txt"
OUTPUT_TEXT = "processed_output.txt"
CSV_FILE = "records.csv"
JSON_FILE = "records.json"

SAMPLE_RECORDS = [
    {"id": 1, "name": "Alice", "score": 92},
    {"id": 2, "name": "Ben", "score": 85},
    {"id": 3, "name": "Carmen", "score": 78},
]


def read_text_file(path: str) -> list[str]:
    with open(path, "r", encoding="utf-8") as f:
        return f.readlines()


def write_text_file(path: str, lines: list[str]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.writelines(lines)


def write_csv_file(path: str, records: list[dict]) -> None:
    if not records:
        return

    fieldnames = list(records[0].keys())
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)


def read_csv_file(path: str) -> list[dict]:
    with open(path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)


def write_json_file(path: str, data: list[dict]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def read_json_file(path: str) -> list[dict]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main() -> None:
    if not os.path.exists(SOURCE_TEXT):
        print(f"Source text file not found: {SOURCE_TEXT}")
        return

    lines = read_text_file(SOURCE_TEXT)
    processed = [line.upper() for line in lines]
    write_text_file(OUTPUT_TEXT, processed)
    print(f"Read {len(lines)} lines and wrote {len(processed)} lines to {OUTPUT_TEXT}")

    write_csv_file(CSV_FILE, SAMPLE_RECORDS)
    print(f"Wrote {len(SAMPLE_RECORDS)} records to {CSV_FILE}")

    rows = read_csv_file(CSV_FILE)
    print(f"Loaded {len(rows)} records from CSV:")
    print(rows)

    write_json_file(JSON_FILE, SAMPLE_RECORDS)
    print(f"Wrote records to {JSON_FILE}")

    json_data = read_json_file(JSON_FILE)
    print("Loaded first JSON record:")
    print(json_data[0])


if __name__ == "__main__":
    main()
