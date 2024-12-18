
import random
import string
character_list=""
password=[]
print("Please write a number you want to determine your password length")
pswdlength=int(input())
valid_int = {1,2,3}

print('''Choose password strong level 
         level 1
         level 2
         level 3 ''')
while True:
 pswdlevel=int(input())
 if pswdlevel in valid_int:
  break
 else:
  print("Please write valid value")



if pswdlevel==1:
  character_list += string.digits
  for i in range(pswdlength):
   randomdigit=random.choice(character_list)
   password.append(randomdigit)
elif pswdlevel==2:
 for x in range(pswdlength):
  selector=random.randint(0,1)
  if selector==1:
   character_list += string.digits
   randomdigit=random.choice(character_list)
   password.append(randomdigit)
  else:
   character_list+=string.ascii_letters
   randomletter=random.choice(character_list)
   password.append(randomletter)
else:
 for x in range(pswdlength):
  selector=random.randint(0,2)
  if selector==1:
   character_list += string.digits
   randomdigit=random.choice(character_list)
   password.append(randomdigit)
  elif selector==2:
   character_list+=string.ascii_letters
   randomletter=random.choice(character_list)
   password.append(randomletter)
  else:
   character_list+=string.punctuation
   randompunctuation=random.choice(character_list)
   password.append(randompunctuation)

print(f"Password:{"".join(password)}")
   

 
    


