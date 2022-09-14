#Pokemon Quiz game

print("Welcome to Sam's PokeQuiz!")

#Scorekeeping
score=0
#Start the play sequence
playing=input("Would you like to play? ")
if playing!= "yes":
    quit()
print("Let's begin :) ")

#Question 1
answer1=input("What is the Unova region's grass-type starter? ")
if answer1=="Snivey":
    print("Correct!")
    score=score+1
else:
    print("Incorrect :(")

#Question 2
answer2=input("How many evolutions of Eevee exist as of Gen 8 (SW/SH)? ")
if answer2=="8":
    print("Correct!")
    score=score+1
else:
    print("Incorrect :(")

#Question 3
answer3=input("What item does Dusclops need to evolve into Dusknoir? ")
if answer3=="Reapers cloth":
    print("Correct!")
    score=score+1
else:
    print("Incorrect :(")

#Question 4
print("Final question! This one is worth two points, but will subtract one point each time you get it wrong.")
answer4 = input("What is the nickname of Lilly's Cosmog in Pokemon Sun/Moon? ")
while True:
    if answer4!="Nebby":
        print("Incorrect! Hint: Its name is related to a galactic formation.")
        score=score-1
        answer4 = input("What is the nickname of Lilly's Cosmog in Pokemon Sun/Moon? ")
    else:
        print("Correct!")
        score=score+2
        break

#End game
score=str(score)
print("You've reached the end!")
useless=input("How did you think you did? ")
print("Here is your score: "+ score)
print("Play again soon!")