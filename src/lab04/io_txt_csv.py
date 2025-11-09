import csv
from pathlib import Path
from typing import Iterable, Sequence

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    return p.read_text(encoding=encoding)

def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    rows_list = list(rows)

    if rows_list:
        first_length = len(rows_list[0])
        for i, row in enumerate(rows_list):
            if len(row) != first_length:
                raise ValueError(f"Строка {i} имеет длину {len(row)}, ожидалась {first_length}")
    p.parent.mkdir(parents=True, exist_ok=True)

    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if header is not None:
            writer.writerow(header)
        writer.writerows(rows_list)

def ensure_parent_dir(path: str | Path) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True) #убрать этот лишний фрагмент кода, есть дальше

if __name__ == "__main__":
    print("Тестирование функций")

    input_path = "../../data/input.txt"
    csv_path = "../../data/check.csv"

    ensure_parent_dir(input_path)
    ensure_parent_dir(csv_path)

    try:
        txt = read_text(input_path)
        print("read_text работает:")
        print(f"Прочитано: {repr(txt)}")
    except FileNotFoundError:
        print("Файл не найден!")
    except Exception as e:
        print(f"Ошибка в read_text: {e}")

    try:
        write_csv([("word", "count"), ("test", 3)], csv_path)
        print("write_csv работает:")
    except Exception as e:
        print(f"Ошибка в write_csv: {e}")
    print("Тестирование завершено")