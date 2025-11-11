Лабораторная работа 5
Задание А

```
import json
import csv
from pathlib import Path

def json_to_csv(json_path: str, csv_path: str) -> None:
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if not data or not isinstance(data, list):
        raise ValueError("Пустой JSON")

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
```

json to csv

Файл на вход:

<img width="298" height="333" alt="image" src="https://github.com/user-attachments/assets/29d7a1d7-7942-4f89-8b9e-165eda3ad1d9" />

Файл на выход:

<img width="155" height="80" alt="image" src="https://github.com/user-attachments/assets/78579fe7-5196-46df-b91e-fd7c725afa7b" />


csv to json

Файл на вход:

<img width="155" height="80" alt="image" src="https://github.com/user-attachments/assets/78579fe7-5196-46df-b91e-fd7c725afa7b" />

Файл на выход:

<img width="298" height="333" alt="image" src="https://github.com/user-attachments/assets/29d7a1d7-7942-4f89-8b9e-165eda3ad1d9" />



Задание В


```
import csv
from pathlib import Path


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:

    if not Path(csv_path).exists():
        raise FileNotFoundError(f"Файл {csv_path} не найден")

    with open(csv_path, encoding="utf-8") as f:
        data = list(csv.reader(f))

    if not data:
        raise ValueError("CSV файл пустой")

    from openpyxl import Workbook
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    for row in data:
        ws.append(row)

    for column in ws.columns:
        max_length = 0
        for cell in column:
            if cell.value:
                max_length = max(max_length, len(str(cell.value)))
        ws.column_dimensions[column[0].column_letter].width = max(max_length + 2, 8)

    wb.save(xlsx_path)

if __name__ == "__main__":
    base_dir = Path(__file__).parent.parent.parent

    try:
        csv_to_xlsx(
            str(base_dir / "data" / "samples" / "people.csv"),
            str(base_dir / "data" / "out" / "people.xlsx")
        )
        print("CSV → XLSX")
    except Exception as e:
        print(f"{e}")

```


<img width="341" height="190" alt="image" src="https://github.com/user-attachments/assets/6baf920c-853a-4cde-b292-b3dac3df9e58" />




















Лабораторная работа 1
#задание 1
<img width="1920" height="1030" alt="img01" src="https://github.com/user-attachments/assets/29bfdd0d-0ab4-4e5e-9758-3920f317cc50" />

#задание 2
<img width="1920" height="1030" alt="img02" src="https://github.com/user-attachments/assets/13a88d34-4568-45ae-8638-71384d2798a9" />

#задание 3
<img width="1920" height="1030" alt="img03" src="https://github.com/user-attachments/assets/881da6a6-2c49-4f0f-80bf-c20c19d909b8" />

#задание 4
<img width="1920" height="1030" alt="img04" src="https://github.com/user-attachments/assets/fe73003b-2339-43fb-81d9-066586fa302f" />

#задание 5
<img width="1920" height="1030" alt="img05" src="https://github.com/user-attachments/assets/8fd9699b-1085-4da4-b87b-736a1c7915ec" />
