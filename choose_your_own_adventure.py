print("WELCOME TO MY adventure game!")

playing = input("Do you want to play ? ")

if playing.lower() != "yes":
    quit()

name = input("What is your name ? ").title()
print("Hello", name, "wlcome to this adventure!")

player = input((str(name) + ' you are alone in mysterious forest and you had to take a path(left/right), which path will u take ? ')).lower()

if player == "right":
    player = input("You met yourself at the edge of the ocean and saw a canoe and a bridge, will you cross over with the canoe or walk on the bridge(walk/cross) ? ").lower()
    
    if player == "cross":
        print("While crossing, the canoe got hit by a rock and it sinks, so u lose!")
    
    elif player == "walk":
        player = input("After walking for a while..., you later met a stranger and the stranger ask for help, will you help or leave ? ").lower()

        if player == "help":
            print("After helping him then he tells you that the only way out is to break this orb and you will dissappear to where you came from, so he said 'this is a mysterious place and there is no other way out'. so he dissappears")
            print("You won this Adventure! :) .")
        
        elif player == "leave":
            print("You keep walking and walking.., then you met a snake along the road that eates you and you died instantly")
            print("You lose this Adventure! :( .")
        
        else:
            print("Invalid input option!")
    else:
        print()

elif player == "left":
    player = input("You met yourself in a wide area so you saw a cave, do want to enter or leave ? ").lower()

    if player == "enter":
        player = input("When you enter the cave you saw two doors(white, black) which one will u enter ? ").lower()

        if player == "white":
            print("Thousands of snakes rush to u and eat all your flesh and you died")
            print("You lose this Adventure! :(.")

        elif player == "black":
            print("You saw a stranger sitting, which then gave you an orb to break inorder for you to dissappear from where you came from.")
        
        else:
            print("Invalid input option!")

    elif player == "leave":
        print("You run into a python which eates you and you died instantly")
        print("You lose this Adventure! :(.")

    else:
        print("Invalid input option!")

else:
    print("Invalid input option!")

