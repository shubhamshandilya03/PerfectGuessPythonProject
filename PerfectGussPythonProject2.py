import random
randnumber = random.randint(1, 100)
# print(randnumber)
userguess = None
noOfGuesses = 0
while(userguess != randnumber):
    userguess = int(input("Enter Your Guess:"))
    noOfGuesses += 1
    if(userguess == randnumber):
        print("You Guessed it Correct!!!")
    else:
        if(userguess > randnumber):
            print("You Guessed it Wrong!!!Guess smaller number...")
        else:
            print("You Guessed it Wrong!!!Guess Larger number...")
print(f"You guessed the number in {noOfGuesses} Guesses...")

with open("HighScore.txt", "r") as f:
    hiscore = int(f.read())

# print(hiscore)
if(hiscore > noOfGuesses):
    print("You have Just Broken the record of Guesses...")
    with open("HighScore.txt", "w") as f:
        f.write(str(noOfGuesses))
