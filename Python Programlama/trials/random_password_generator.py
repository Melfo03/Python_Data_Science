import random
import string
character_list=""
password=[]
print("Please write a number you want to determine your password length")
pswdlength=int(input())
valid_chars = {'y','n'}

print("Do you want to have your password include a character (y/n)")
while True:
 pswdcharacter=input()
 if pswdcharacter in valid_chars and len(pswdcharacter)==1:
  break
 else:
  print("Please write valid value")
pswdcharacter_value=ord(pswdcharacter)


if pswdcharacter_value==110:
  character_list += string.digits
  for i in range(pswdlength):
   randomdigit=random.choice(character_list)
   password.append(randomdigit)
elif pswdcharacter_value==121:
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

print(f"password:{"".join(password)}")
   

 
    


