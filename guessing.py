import random as rd

randomNumber = rd.randint(0, 10);
flag = False

while flag != True: 

    guessNum = int(input("Guess the number from 0 to 10: "))
    
    if randomNumber == guessNum:
        flag = True
        print("You'd guess the number!")
    elif randomNumber > guessNum:
        print("Guess Larger")
    elif randomNumber < guessNum:
        print("Guess Smaller")




