import random

secret = random.randint(1, 10)  # secret number

while True:
    guess = int(input("Guess the number (1-10): "))
    if guess == secret:
        print("🎉 Correct! You guessed it.")
        break
    elif guess < secret:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")
