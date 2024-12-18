import tkinter as tk
from tkinter import messagebox

def getter():
    try:
        
        global veri
        veri=int(entry_1.get())
    
        
    except ValueError:
        messagebox.showerror("Hata", "Lütfen bir tamsayı girin.")
def selection():
  global selections
  selections=varr.get()
  

def copy_to_clipboard(event):
    # Label'daki metni al
    master.clipboard_clear()  # Önce panoyu temizle
    if result_label.cget("text")=="Kopyalandı!":
      result_label.config(text="")
    else:
     master.clipboard_append(result_label.cget("text"))  # Metni panoya ekle
     result_label.config(text="Kopyalandı!")  # Kullanıcıya geri bildirim ver

  
 
    
    
master=tk.Tk()
master.title("Password Genarator")

canvas=tk.Canvas(master,bg="black",height=800,width=800)
canvas.pack(fill=tk.BOTH, expand=True)

üst_frame=tk.Frame(master,bg="red")
üst_frame.place(x=200,y=200,relwidth=0.5,relheight=0.5)
sag_frame=tk.Frame(master,bg="white")
sag_frame.pack(side=tk.LEFT, fill=tk.X)


varr=tk.IntVar()



rb1=tk.Radiobutton(üst_frame,text="Level 1",variable=varr,value=1,command= lambda:selection()).pack()
rb2=tk.Radiobutton(üst_frame,text="Level 2",variable=varr,value=2,command= lambda:selection()).pack()
rb3=tk.Radiobutton(üst_frame,text="Level 3",variable=varr,value=3,command= lambda:selection()).pack()
entry_1=tk.Entry(master)
entry_1.pack()
b2=tk.Button(master,text="Göner",command=lambda:getter()).pack()
veri=int()
selections=int()
sayii2=2
sayi1=20
result_label = tk.Label(master, text="")
result_label.pack(pady=10)
result_label.bind("<Button-1>",copy_to_clipboard)


b1=tk.Button(master,text="Olustur",command=lambda:generator(veri,selections)).pack(pady=50)
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
 result_label.config(text=f"Password:{"".join(password)}",state="normal")
 return password


master.mainloop()
