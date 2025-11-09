Задание A — модуль src/lab04/io_txt_csv.py

```
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
    p.parent.mkdir(parents=True, exist_ok=True)

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
```
<img width="842" height="83" alt="image" src="https://github.com/user-attachments/assets/91c4d6cc-11e3-449d-9177-2724eb6ed746" />


<img width="814" height="103" alt="image" src="https://github.com/user-attachments/assets/24764e7e-6127-4c78-bd99-0de11f1f77b6" />

Задание B — скрипт src/lab04/text_report.py

```
from io_txt_csv import read_text, write_csv
from src.lib.text import normalize, tokenize, count_freq, top_n
from pathlib import Path

current_dir = Path(__file__).parent
project_root = current_dir.parent.parent
input_path = project_root / "data" / "input.txt"

text = read_text(str(input_path))
print(text)

norm = normalize(text)
tokens = tokenize(norm)
freq = count_freq(tokens)
top_5 = top_n(freq, 5)

output_path = project_root / "data" / "report.csv"
write_csv(top_5, str(output_path), header=('word', 'count'))

print(f'Всего слов: {len(tokens)}')
print(f'Уникальных слов: {len(freq)}')
print('Топ-5:')
for word, count in top_5:
    print(f'{word}: {count}')
```

<img width="849" height="138" alt="image" src="https://github.com/user-attachments/assets/b8d5995d-5567-44ba-a7ec-3e2965394a5e" />



<img width="550" height="347" alt="image" src="https://github.com/user-attachments/assets/d275ba05-6b59-4d90-baeb-7898b129c36c" />





