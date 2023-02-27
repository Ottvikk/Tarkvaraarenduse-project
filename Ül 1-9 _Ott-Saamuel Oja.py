"""
#Ül 1

a = 1 #Vajalikud andmed
b = "a/n"
while a < 3: #While tsükkel
    print(b) #Prindib b
    a +=1 #Kui siia jõuab siis liidab iga kord 1 juurde
"""
"""
#Ül2

b = "'Tere!'" #Vajalikud andmed
c = '"Head aega!"'
print(b) #Prindib välja tulemused
print("\n")
print(c)
"""
"""
#Ül 3

a = "Tere" #Vajalikud andmed
b = "Tore"
lause = a * 3 + "\\" + b
print(lause) #Prindib välja tulemused
"""
"""
#Ül 4

nimi = "loomariik" #Vajalikud andmed
print(nimi[0] + nimi[-1]) #Prindib välja tulemused
"""
"""
#Ül 5

nimi1 = "Paide" #Vajalikud andmed
nimi2 = "Türi"
print("Tere,"[0],nimi1[-5],nimi2,"!") #Prindib välja tulemused
"""
"""
#Ül 6

a = "A" #Vajalikud andmed
b = 1
while b < 3: #Algab While tsükkel
    print(a,end=" ") #Prindib välja tulemused
    b += 1 #Liidab iga kord kui siia jõuab b-le 1 juurde
"""
"""
#Ül 7

a = 10 #Vajalikud andmed
b = 2
print(a > b) #Prindib välja tulemused
"""
"""
#Ül 8

a = 10 #Vajalikud andmed
b = 2
print(a != b and b > 10) #Prindib välja tulemused
print(b == a or a >= 0)
"""
"""
#Ül 9

from tkinter import * #impordib tkinteri
raam = Tk() #defineerib sõna raam
raam.title("Tühi tahvel") #Paneb pealkirja
tahvel = Canvas(raam, width=600) #Raami suurus

tahvel.create_rectangle(50,70,100,100, width=2, outline="blue") #Joonistab ruudu siniste äärtega
tahvel.create_text(50,50, text="Tere!") #Kirjutab teksti 

tahvel.create_polygon(100,100,150,150,200,100, fill="red",outline="black") #Joonistab hulknurga seest on punane ja väljast on must
tahvel.pack()
raam.mainloop()
"""