def format_record(rec):
    fio, group, gpa = rec

    if not fio.strip():
        raise ValueError("Пустое ФИО")
    if not group.strip():
        raise ValueError("Пустая группа")
    if not isinstance(gpa, (int, float)):
        raise ValueError("Неверный тип GPA")

    fio_parts = fio.strip().split()
    surname = fio_parts[0].title()

    initials = ""
    for part in fio_parts[1:]:
        initials += part[0].upper() + "."

    gpa_str = f"{gpa:.2f}"

    return f"{surname} {initials}, гр. {group}, GPA {gpa_str}"


tests = [
    ("Иванов Иван Иванович", "BIVI-25", 4.6),
    ("Петров Пётр", "IKBO-12", 5.0),
    ("Петров Петр Петрович", "IKBO-12", 5.0),
    ("  сидорова  анна   сергеевна ", "ABB-01", 3.999),
]

for test in tests:
    print(format_record(test))

print("Тесты ошибок")
error_tests = [
    ("", "GROUP-1", 4.0),  # пустое ФИО
    ("Иванов Иван", "", 4.0),  # пустая группа
    ("Иванов Иван", "GROUP-1", "5"),  # неверный GPA
]

for test in error_tests:
    try:
        print(format_record(test))
    except ValueError as inv:
        print(f"ValueError: {inv}")
