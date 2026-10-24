scores = [12, 17, 9, 15, 14]
largest_score = 0
student = 0

for i, item in enumerate(scores,start=1):
    if item > largest_score:
        largest_score = item
        student = i

print(f"Best: {largest_score} (student #{student})")