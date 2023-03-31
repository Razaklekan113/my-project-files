import random
print("WELCOME TO MY ROCK,PAPER AND SCISSORS GAME :)")

playing = input("Do you want to play ? ")

if playing.lower() != "yes":
    print("Goodbye for now!")
    quit()

print("LET'S PLAY :) ")

computer_wins = 0
player_wins = 0

option = ["rock", "paper", "scissors"]

while True:
    player = input("pick either rock/paper/scissors and q to quit to know your score: ")
    if player.lower() == "q":
        break
    
    if player not in option:
        print("please choose either rock/paper/scissors")
        continue
    
    random_number = random.randint(0,2)
    
    computer_picked = option[random_number]
    print("computer picked...." , computer_picked + ".")

    if player == "rock" and computer_picked == "scissors":
        print("You won!")
        player_wins += 1
    
    elif player == "paper" and computer_picked == "rock":
        print("You won!")
        player
        player_wins += 1
    
    elif player == "scissors" and computer_picked == "paper":
        print("You won!")
        player_wins += 1
    
    elif player == "rock" and computer_picked == "rock":
        print("it's a tie!")

    elif player == "scissors" and computer_picked == "scissors":
        print("it's a tie!")

    elif player == "paper" and computer_picked == "paper":
        print("it's a tie!")

    else:
        print("You lose!")
        computer_wins += 1


print("You won", player_wins, " times")
print("computer won", computer_wins, " times")
print("Goodbye")