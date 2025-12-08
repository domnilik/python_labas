from src.lib.text import normalize, tokenize, count_freq, top_n
import sys


def main():
    text = sys.stdin.read()
    if not text.strip():
        print("Нет входных данных")
        return
    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)

    if not tokens:
        print("В тексте не найдено слов")
        return

    total_words = len(tokens)
    freq_dict = count_freq(tokens)
    unique_words = len(freq_dict)
    top_words = top_n(freq_dict, 5)

    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    for word, count in top_words:
        print(f"{word}: {count}")


if __name__ == "__main__":
    test_text = "Привет, мир! Привет!!!"

    print('$ echo "Привет, мир! Привет!!!" | python src/text_stats.py')
    normalized = normalize(test_text)
    tokens = tokenize(normalized)
    freq = count_freq(tokens)
    top = top_n(freq, 5)
    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word, count in top:
        print(f"{word}:{count}")
