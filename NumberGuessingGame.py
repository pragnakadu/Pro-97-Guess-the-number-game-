import random
number=random.randint(1,9)
chances=0
print("Number Guessing Game!!")
print("Guess a number between 1-9:")

while chances<5 :

        guess=int(input ("Enter a number:"))
 
        if guess == number:
                    print("You win the game!!!!")
                    break

        elif guess < number :
                print("TryAgain,your number was very low.Your number:",guess)
                
        else:
                print("TryAgain,your number was very high.Your number:",guess)
        
        chances += 1

if not chances < 5 :
        print("You loose, better luck next time , Number:" , number)
