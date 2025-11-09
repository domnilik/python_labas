import json
import csv
from pathlib import Path

def json_to_csv(json_path: str, csv_path: str) -> None:
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if not data or not isinstance(data, list):
        raise ValueError("Пустой JSON или неподдерживаемая структура")

    fields = sorted(set().union(*(item.keys() for item in data)))

    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for item in data:
            writer.writerow({field: item.get(field, '') for field in fields})

def csv_to_json(csv_path: str, json_path: str) -> None:
    with open(csv_path, 'r', encoding='utf-8') as f:
        data = list(csv.DictReader(f))

    if not data:
        raise ValueError("CSV файл пустой")

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    base_dir = Path(__file__).parent.parent.parent

    people_json = base_dir / "data" / "samples" / "people.json"
    people_csv = base_dir / "data" / "samples" / "people.csv"
    output_csv = base_dir / "data" / "out" / "people_from_json.csv"
    output_json = base_dir / "data" / "out" / "people_from_csv.json"

    (base_dir / "data" / "out").mkdir(exist_ok=True)

    try:
        json_to_csv(str(people_json), str(output_csv))
        print("JSON → CSV")

        csv_to_json(str(people_csv), str(output_json))
        print("CSV → JSON")

    except Exception as e:
        print(f"{e}")