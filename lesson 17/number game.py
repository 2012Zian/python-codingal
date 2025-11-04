import random

playing = True
number = str(random.randint(10,20))

print("i will generate a number 0 to 10 you have to guess the number!:")

while playing:
    guess = input("give me your best guess")
    if number == guess:
        print("you win the game")
        print("the number was",number)
        break
    else:
        print("you guessed wrong try again")