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
write_csv(top_5, str(output_path), header=("word", "count"))

print(f"Всего слов: {len(tokens)}")
print(f"Уникальных слов: {len(freq)}")
print("Топ-5:")
for word, count in top_5:
    print(f"{word}: {count}")
