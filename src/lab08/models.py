# imports
from dataclasses import dataclass
from datetime import datetime, date

@dataclass #декоратор (упрощает инициализацию класса, автоматически создает функции __init__ и __repr__ )
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        if isinstance(self.gpa, str) or self.gpa < 0 or self.gpa > 5:
            raise ValueError('Invalid GPA-score')
        try:
            self._date_of_birth_ = datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid birthdate")

    def age(self) -> any:
        return date.today().year - self._date_of_birth_.year

    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }

    @classmethod
    def from_dict(cls, d: dict):
        return Student(d["fio"], d["birthdate"], d["group"], d["gpa"])

    def __str__(self):
        return f'Obj Student. fio: {self.fio}, birthdate: {self.birthdate}, group: {self.group}, gpa: {self.gpa}'

