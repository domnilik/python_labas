def min_max(x: list) -> tuple:

    if not x:
        raise ValueError

    return (min(x), max(x))


test_cases = [[3, -1, 5, 5, 0], [42], [-5, -2, -9], [], [1.5, 2, 2.0, -3.1]]

print("Тестирование min_max")
for i, test_data in enumerate(test_cases, 1):
    try:
        result = min_max(test_data)
        print(f"{i}: {test_data} -> {result}")
    except ValueError as e:
        print(f"{i}: {test_data} -> {e}")


def unique_sorted(nums):

    return sorted(set(nums))


test_cases = [[3, 1, 2, 1, 3], [], [-1, -1, 0, 2, 2], [1.0, 1, 2.5, 2.5, 0]]

print("Тестирование unique_sorted")
for test in test_cases:
    result = unique_sorted(test)
    print(f"{test} -> {result}")


def flatten(mat):
    result = []

    for item in mat:
        if not isinstance(item, (list, tuple)):
            raise TypeError(f"Элемент {item} не является списком или кортежем")

        result.extend(item)

    return result


test_cases = [
    [[1, 2], [3, 4]],
    [[1, 2], (3, 4, 5)],
    [[1], [], [2, 3]],
    [[1, 2], "ab"],  # вызывает TypeError
]

print("Тестирование flatten")
for test in test_cases:
    try:
        result = flatten(test)
        print(f"{test} -> {result}")
    except TypeError as e:
        print(f"{test} -> TypeError: {e}")
