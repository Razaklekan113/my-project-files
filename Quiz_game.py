print("WELCOME TO MY COMPUTER QUIZ GAME!")

playing = input("Do you want to play ? ")

if playing.lower() != "yes":
    quit()

print("Ok then let's play :)")
score = 0

answer = input("What is the full meaning of C.P.U ? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("incorrect!")

answer = input("What is the full meaning of R.A.M ? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("incorrect!")

answer = input("What is the full meaning of R.O.M ? ")
if answer.lower() == "read only memory":
    print("Correct!")
    score += 1
else:
    print("incorrect!")

answer = input("What is the full meaning of L.G.A ? ")
if answer.lower() == "local government area":
    print("Correct!")
    score += 1
else:
    print("incorrect!")

answer = input("What is the full meaning of HTTP ? ")
if answer.lower() == "hyper text transfer protocol":
    print("Correct!")
    score += 1

else:
    print("incorrect!")

    #calculating the score
print("You got " + str(score) + " points!")
print("You got " + str((score/5) * 100) + "%")



