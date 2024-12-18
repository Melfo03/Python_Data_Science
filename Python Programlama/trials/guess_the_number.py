import random
guess=random.randint(0,10)
usrguess=0
def comparator(x,y):
    if x==y:
        print("Your guess is correct")
    else:
        print("Your guess is incorrect")
        
while guess!=usrguess:
 print("Guess the number")
 usrguess=int(input())
 comparator(guess,usrguess)
 
 

