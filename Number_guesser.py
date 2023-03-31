import random

print("WELCOME TO MY NUMBER GUSSER GAME!")

playing = input("Do you want to play ? ")

if playing.lower() != "yes":
    quit()

number = input("Enter the range of number to guess from : ")

if number.isdigit():
    number = int(number)

    if number <= 0:
        print("please type a larger number next time")
        quit()

else:
    print("please type a number next time")
    quit()

random_number = random.randint(0, number)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess : ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter a number")
        continue
    
    if user_guess == random_number:
        print("You guessed it right")
        break
    elif user_guess > random_number:
        print("You were above the number")
    else:
        print("You were below the number")

print("You got it in", guesses, "guesses!")