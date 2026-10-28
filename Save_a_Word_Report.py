counts = {}

with open("text.txt", encoding="utf-8") as f:
    for line in f:
        line = line.lower()
        for punc in ".,?!":
            line = line.replace(punc, "")
        for word in line.split():
            counts[word] = counts.get(word, 0) + 1

with open("report.txt", "w", encoding="utf-8") as report:
    report.write(f"Words: {sum(counts.values())}\n")
    report.write(f"Unique: {len(counts)}\n")
    for word in sorted(counts):
        report.write(f"{word} {counts[word]}\n")