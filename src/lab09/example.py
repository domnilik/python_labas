from group import Group
from src.lab08.models import Student

g = Group(r"C:\Users\huawei\PycharmProjects\python_labas\data\lab09\student.csv")

print("=== list() ===")
print(*g.list()[:3], sep="\n")

print("\n=== add() ===")
s = Student("Тестовый Студент", "2005-05-05", "TEST-01", 4.5)
g.add(s)
print("Добавлен:", s)

print("\n=== find('Тест') ===")
print(g.find("Тест"))

print("\n=== update() ===")
g.update("Тестовый Студент", gpa="4.9")
print(g.find("Тест"))

print("\n=== remove() ===")
g.remove("Тестовый Студент")
print(g.find("Тест"))


