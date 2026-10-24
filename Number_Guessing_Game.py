import random

secret = random.randint(1, 100)
attempts = 0

while attempts < 7:
    attempts += 1
    guess = int(input("Your guess: "))
    if guess == secret:
        print(f"Bravo! You found it in {attempts} attempts")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")

if attempts == 7: 
    print(f"Lost! It was, {secret}")
