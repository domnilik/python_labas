import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n

@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПриВЕТ\nМир\t", "привет мир"),
        ("Ёжик, Ёлка", "ежик, елка"),
        ("Hello\n\nWorld", "hello world"),
        (" двойные пробелы ", "двойные пробелы"),
    ],
)
def test_normalize_basic(source, expected):
    assert normalize(source) == expected

@pytest.mark.parametrize(
    "source, expected",
    [
        ("привет мир", ["привет", "мир"]),
        ("ёжик, ёлка", ["ёжик", "ёлка"]),
    ],
)
def test_tokenize_basic(source, expected):
    assert tokenize(source) == expected

def test_count_freq_and_top_n():
    tokens = ["самолет", "машина", "самолет", "машина", "машина"]
    freq = count_freq(tokens)
    top = top_n(freq, 2)

    assert top == [("машина", 3), ("самолет", 2)]

def test_top_n_tie_breaker():
    freq = {"самолет": 3, "машина": 3, "вертолет": 3}
    top = top_n(freq, 3)

    assert top == [("вертолет", 3), ("машина", 3), ("самолет", 3)]


