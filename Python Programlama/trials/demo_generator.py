def generator(pswdlength,pswdlevel):
    
 import random
 import string
 character_list=""
 password=[]
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
   
generator(5,3)

 
    


