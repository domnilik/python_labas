import argparse
from pathlib import Path
from src.lib.text import normalize, tokenize, count_freq, top_n

def cmd_cat(path, numbered=False):
    with open(path, encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            print(f"{i}\t{line.rstrip()}" if numbered else line.rstrip())

def stats(path, topk):
    text = Path(path).read_text(encoding="utf-8")
    text = normalize(text)
    tokens = tokenize(text)
    freq = count_freq(tokens)
    top = top_n(freq, topk)

    print(f"Всего слов: {len(tokens)}")
    print(f"Различных слов: {len(freq)}\n")
    print(f"Топ-{topk} слов:")
    for word, cnt in top:
        print(f"{word}: {cnt}")

def main():
    parser = argparse.ArgumentParser(description="CLI-converter")
    subparsers = parser.add_subparsers(dest="command", required=True)

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()

    if args.command == "cat":
        cmd_cat(args.input, args.n)
    elif args.command == "stats":
        stats(args.input, args.top)

if __name__ == "__main__":
    main()
