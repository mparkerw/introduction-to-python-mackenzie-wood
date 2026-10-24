answers = ["b","a","d","c"]
corrects = ["b","c","d","a"]

right = 0
total = 0

for answer, correct in zip(answers, corrects):
    total += 1
    if answer == correct:
        right += 1

print(f"Score: {right}/{total}")