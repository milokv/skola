from random import randrange
num = randrange(100)
guess = 0
guesscount = 0
guesslimit = 8
outofguess = False
while guess != num and not(outofguess):
    if guesscount >= guesslimit:
        outofguess = True
    guess = int(input("guess number"))
    if guess > num:
        print("Lower")
    elif guess < num:
        print("Higher")
    guesscount += 1

if outofguess == True:
    print("lose")
else: print("win")





