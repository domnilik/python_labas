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
