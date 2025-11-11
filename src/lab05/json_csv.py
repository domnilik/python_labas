import json
import csv
from pathlib import Path

def json_to_csv(json_path: str, csv_path: str) -> None:
    json_path = Path(json_path)
    csv_path = Path(csv_path)

    if not json_path.exists(): raise ValueError("Входной файл не существует")
    if json_path.suffix != ".json": raise ValueError(f'Неверное расширение файла "{json_path.suffix}"')
    if csv_path.suffix != ".csv": raise ValueError(f'Неверное расширение файла "{csv_path.suffix}"')

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f) #читаем JSON файл и превращаем в питоновские данные (списки, словари), обозначаем это как data

    if not data or not isinstance(data, list): #если data не является списком
        raise ValueError("Пустой JSON")

    fields = sorted(set().union(*(item.keys() for item in data))) #сортируем все названия полей из всех записей, убираем повторы

    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fields) #создаем писателя
        writer.writeheader() #напиши заголовок
        for item in data:
            writer.writerow({field: item.get(field, '') for field in fields}) #пробуем найти поле field в записи, если не находим, выводим пустую строку

def csv_to_json(csv_path: str, json_path: str) -> None:
    json_path = Path(json_path)
    csv_path = Path(csv_path)

    if not csv_path.exists(): raise ValueError("Входной файл не существует")
    if json_path.suffix != ".json": raise ValueError(f'Неверное расширение файла "{json_path.suffix}"')
    if csv_path.suffix != ".csv": raise ValueError(f'Неверное расширение файла "{csv_path.suffix}"')

    with open(csv_path, 'r', encoding='utf-8') as f:
        data = list(csv.DictReader(f)) #превращаем в обычный список словарей. Dictreader - читатель, который понимает все заголовки

    if not data:
        raise ValueError("CSV файл пустой")

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2) #json.dump - записываем данные в файл, ensure_ascii=False - русские буквы остаются русскими, indent=2 - красивые отступы

if __name__ == "__main__":
    base_dir = Path(__file__).parent.parent.parent #определяем базовую папку, поднимаемся на 3 уровня вверх от файла

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