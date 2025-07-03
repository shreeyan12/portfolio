import random
number = random.randint(1, 20)
a = 5

print("Guess the number (1-20)")
print(f"You have {a} chances to guess it.")

for i in range(1, a + 1):
    guess = int(input(f"Attempt {i}: Enter your guess: "))
    if guess == number:
        print("🎉 Correct!")
        break
    elif guess < number:
        print("Too low")
    else:
        print("Too high")
else:
    print(f"😞 Game over. The number was {number}.")
