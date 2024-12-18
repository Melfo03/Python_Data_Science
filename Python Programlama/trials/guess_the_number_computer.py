import random
usrnumber=11
while usrnumber<0 or usrnumber>10:
 print("Write a number between 0 to 10")
 usrnumber=int(input())
guess=11
def comparator(x,y):
 if x==y:
  print("Computer knew your guess")
 else:
  print("Computer did not know your guess")
while usrnumber!=guess:
 guess=random.randrange(11)
 print("Computer guess: ",guess)
 comparator(usrnumber,guess)
  
