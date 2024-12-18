# -*- coding: utf-8 -*-
# =============================================================================
# SAYILAR VE STRINGLER
# =============================================================================
print("Hello")

type(9)
type(5.1)

"A"+"B"
"A"+" B"
"A "*9

name="Hanbey Ozan Kirmizigul"
len(name)
##STRING METODLARI##

#BUYUK KUCUK HARF ISLEMLERI
name="Hanbey Ozan Kirmizigul"
name.isupper()#Buyuk Harflerden Mi
name.islower()#Küçük Harflerden Mi Oluşuyor Sorgusu
name.upper()#Bütün İfadeyi Büyük Harfe Çevirir
name.lower()#Bütün İfadeyi Küçük Harfe Çevirir


#replace()

name="Hanbey Ozan Kirmizigul"
name.replace("a","e")
name.replace(" ","_")


#strip() Kirpma islemleri
name=" Hanbey Ozan Kirmizigul "
name.strip()
name_2="**Hanbey Ozan Kirmizigul**"
name_2.strip("*")
# =============================================================================

##METODLARA GİRİŞ

name="Hanbey Ozan Kirmizigul"
dir(name)#Girilen Değişkende Kullanılabilicek Metodlar Listeler


#substring()
name="Hanbey Ozan Kirmizigul"
name[0]
name[0:3]


#Type Dönüşümleri

birinci=input("Sayi Giriniz")
ikinci=int(input("Sayi Giriniz"))
float(birinci)


#Print()
print("Hanbey","Ozan",sep="_")

# =============================================================================
# VERİ YAPILARI
# =============================================================================

#LİSTLER

notlar=[60,27,"Girmedi"]
total=[notlar,80,90]
total[0]
total[0][2]


isim=["ahmet","mehmet","celal","samet"]
isim[1]="veli"

isim[0:3]="a","b","c"#Eleman Değiştirme
isim=isim+["recep"]#Eleman Ekleme
del isim[0]#Eleman Silme

#append() ve remove()
isim=["ahmet","mehmet","celal","samet"]
isim.append("ozan")#Eleman Ekleme
isim.remove("mehmet")#Eleman Silme


#insert() ve pop()
isim=["ahmet","mehmet","celal","samet"]
isim.insert(0,"enes")#0.İndise Eleman Ekleme
isim.pop(0)

#count() 
isim=["ahmet","ahmet","ahmet","mehmet","mehmet"]
isim.count("ahmet")#Liste İçinde Kaç Tane ahmet değerinin olduğunu sayar
isim.count("mehmet")

#copy()
isim=["ahmet","mehmet","celal","samet"]
yeni_liste=isim.copy()

#extend()
isim=["ahmet","mehmet","celal","samet"]
isim.extend([1,2,3])
isim

#index()
isim=["ahmet","mehmet","samet","celal"]
isim.index("ahmet")

#reverse()
isim=["ahmet","mehmet","samet","celal"]
isim.reverse()#Listeyi Ters Çevirdi

#sort()
liste=[5,4,3,2,1]
liste.sort()#Listeyi Büyükten Küçüğe Sıralar

#clear()
liste=[5,4,3,2,1]
liste.clear()
# =============================================================================


#TUPLE(Demet)
#Tuple'ın Listeden Farkı Değiştirilemez Olmasıdır
#Tuple Oluşturma
t=("ahmet","mehmet",[1,2,3,4])
t_2="ahmet","mehmet",[1,2,3,4]

#Tuple Eleman İşlemleri
t[0]
# =============================================================================

#DİCTİONART(Sözlük)
#Sözlük Oluşturma
sozluk = {"REG" : "Regresyon Modeli",
          "LOJ" : "Lojistik Regresyon",
          "CART" : "Classification and Reg"}

sozluk

len(sozluk)

#Sözlük Eleman İşlemleri

sozluk["REG"]

#Sozluk - Eleman Eklemek & Degistirmek

sozluk = {"REG" : "Regresyon Modeli",
          "LOJ" : "Lojistik Regresyon",
          "CART" : "Classification and Reg"}

sozluk["GBM"] = "Gradient Boosting Mac"
# =============================================================================

#SETLER(Kümeler)
#Sırasız,Unique,Değiştirilebilir

#Set Oluşturma
s=set()
isim=["ahmet","ahmet","ahmet","mehmet","mehmet"]
s=set(isim)

#Setlerde Eleman Ekleme Çıkartma
list=["german","cars"]
s=set(list)
s.add("Audi")
s.add("Bmw")
s.add("Bmw")
s.remove("Bmw")
s.discard("Audi")

#Difference()
set1=set([1,2,5])
set2=set([1,2,3])
set1.difference(set2)#Set1'de Olup Set2'de Olamayan Değeri Getirir
set2.difference(set1)#Set2'de Olup Set1'de Olmayan Değeri Getirir

# Symmetric_difference()
set1=set([1,2,5])
set2=set([1,2,3])
set1.symmetric_difference(set2)#İki Set'de Ortak Olmayan Değerleri Getirir
set2.symmetric_difference(set1)

#İntersection()
set1=set([1,2,5])
set2=set([1,2,3])
set1.intersection(set2)#İki Set'in Kesişim Değerlerini Alır
set2.intersection(set1)

#Union()
set1=set([1,2,5])
set2=set([1,2,3])
set1.union(set2)#İki Setin Birleşimini Alır
set2.union(set1)

# Setlerde Sorgu İşlemleri
set1=set([1,2,3,5])
set2=set([1,2,3])

set1.isdisjoint(set2)#İki Setin Kesişimi Boş Mu Sorgusunu Yapar

set1.issubset(set2)
set2.issubset(set1)#Set2 Deki Bütün Elemanların Set1'in İçinde Olup Olmadığını Sorgular

set1.issuperset(set2)#Set1 Set2'yi Kapsıyor Mu Sorgusunu Yapar
# =============================================================================

# =============================================================================
# ##FONKSİYONLAR
# =============================================================================

#Fonksiyon Tanımlama

def kare_al(x):
    print(x**2)
    
kare_al(9)

def carp(x,y):
    print("Sonuc: "+str(x*y))

carp(11,2)


def topla(x,y):
    return x+y

toplam=topla(5, 8)

# Local Ve Global Değişkenler

x=10#Global Değişken
y=20
def topla(x,y):
    x#Local Değişken
    y
    return x+y

topla(3,2)

# Local Etki Alanından Global Etki Alanını Değiştirmek
liste=[]

def ekle(y):
    liste.append(y)
    print(str(y)+": Eklendi")
    
ekle("Deneme")

# İf & Else
Gelir=20000
Gider=20000

if Gelir>Gider:
    print("Karınız: "+str(Gelir-Gider))
elif Gelir==Gider:
    print("Gelir Gideriniz Eşit")
else:
    print("Borcunuz: "+str(Gider-Gelir))
    
    
# UYGULAMA
#Kişi Adını Gelirini Ve Giderini Alıp Kaydeden Ve Bir Gelir Gider Sonucu Çıkartan Kod
isim=[]
def isim_kaydet(x):
    isim.append(x)
isim_kaydet(input("İsminizi Giriniz: "))

gelir=[]
gider=[]
def gelir_gider_kaydet(x,y):
    gelir.append(x)
    gider.append(y)
gelir_gider_kaydet(int(input("Gelirinizi Girin: ")),int(input("Giderinizi Girin: ")))
str(isim[0])
if gelir>gider:
    print("Sayın "+isim[0]+" Karınız: "+str(gelir[0]-gider[0]))
elif gelir==gider:
    print("Sayın "+str(isim[0])+" Gelir Gider Eşit")
else:
    print("Sayın "+isim[0]+" Zararınız: "+str(gider[0]-gelir[0]))


# =============================================================================
# # DÖNGÜLER
# =============================================================================

#For Döngüsü
for i in range(3):
    print("A")

liste=["a","b","c","d","e"]
for i in liste:
    print(i)

#maaslara yuzde 20 zam yapilacak gerekli kodlari
#yaziniz.

maaslar=[1000,2000,10000]

def zam(x):
    x=x*1.20
    return x

for i in maaslar:
    print("Yeni Maaş: "+str(int(zam(i))))
    
    

#Break Ve Continue
maaslar=[1000,2000,10000,7000,3000]   
maaslar.sort()

for i in maaslar:
    if i==7000:
        break#7000 Değeri Geldiğinde Döngüden Çık
    print(i)
    
    
for i in maaslar:
    if i==7000:
        continue#7000 Değeri Geldiğinde 7000'i Atlayıp Döngüye Devam Et
    print(i)
    
#While

sayi=1
while sayi<=10:
    print(sayi)
    sayi+=1   
    



