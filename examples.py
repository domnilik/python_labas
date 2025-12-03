from src.lab10.linked_list import SinglyLinkedList
from src.lab10.structures import Stack, Queue


lst = SinglyLinkedList()
lst.append(1)
print(f"List: {lst}")

s = Stack()
s.push(2)
print(f"Stack: {s.peek()}")

q = Queue()
q.enqueue(3)
print(f"Queue: {q.peek()}")

print("All classes work correctly")