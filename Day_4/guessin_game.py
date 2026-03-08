import random

secret_number = random.randint(1, 10)

while True:
    guess = int(input("Guess the number (1-10): "))

    if guess == secret_number:
        print("🎉 Correct! You won!")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
      
      