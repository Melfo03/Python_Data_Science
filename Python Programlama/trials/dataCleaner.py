# -*- coding: utf-8 -*-
def satir(a):
    a=a.strip()
    return a
    
def clean(a):
    a=a.replace("'", "")
    a=a.replace(",", "")
    a=a.split()
    return a

def calc(a):
    toplam=0
    sayi=0
    for i in range(420):
      if len(a[i])==2:
        toplam=toplam+int(a[i])
        sayi+=1
    print(toplam/sayi)
        
with open(r"C:\Users\pc\Desktop\sss\not.txt","r") as data:
    data_1 = clean(str([satir(a)for a in data.readlines()]))

calc(data_1)

   
        


