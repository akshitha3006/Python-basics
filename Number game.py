import random
playing = True
number = random.randint(0,9)
print("Welcome to the Number Guessing Game!")
print("I have selected a number between 0 and 9. Can you guess it?")
print("The game ends when u guess the correct number")

while playing:
    guess = int(input("Enter your guess: "))
    if guess == number:
        print("Congratulations! You guessed the correct number:", number)
        break
    else:
        print("Sorry, that's not the correct number. Try again.")
        