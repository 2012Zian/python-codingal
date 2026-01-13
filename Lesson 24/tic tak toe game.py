import random
import time
number=random.randint(1,100)

def intro():
    print("May i ask for your name?")
    global name
    name = input()
    print(name+ ",we are going to play a game. I am thinking of a number between 1 and 100")
    if(number%2==0):
        x='even'
    else:
        x='odd'
    print("\nThis is a",x," number")
    time.sleep(0.5)
    print("go ahead.Guess!")

def pick():
        guessTaken = 0
        while guessTaken < 6:
          time.sleep(.25)
          enter = input("guess: ")
          try: 
              guess = int(enter)
              if guess<=100 and guess>=1:
                  guessTaken=guessTaken+1
                  if guessTaken<6:
                      if guess<number:
                          print("the guess of the number that you have entered is to low")
                      if guess>number:
                          print("the guess of the number that you have entered is to high")
                      if guess !=number:
                          print("try agan!")
                      if guess==number:
                          break
              if guess>100 or guess<1:
                  print("silly goose! that number is not in the range")
                  time.sleep(.25)
                  print("please ent a number between 1 and a 100")
          except:
              print("i dont think that"+enter+" is a number.sorry")
        if guess==number:
            guessTaken = str(guessTaken)
            print("good job,{}! you guessed my number in{} guesses!".format(name,guessTaken))
        if guess != number:
            print("nope. the number i was thinking of was " + str(number))
playagain='yes'
while playagain=="yes" or playagain=="y" or playagain=='Yes':
    intro()
    pick()
    print("do you want to play again")
    playagain = input()
    
