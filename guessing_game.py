import random

jackpot = random.randint(1, 100)
guess = int(input("Guess the number: "))
attemps = 1

while guess != jackpot:
    if guess < jackpot:
        print("Guess higher")
    else:
        print("Guess lower")
    guess = int(input("Guess the number: "))
    attemps += 1

print("Hurray you did it.")
print(f"You took {attemps} attempts.")