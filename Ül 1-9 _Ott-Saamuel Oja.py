"""
#Ül 1
a = 1
b = "a/n"
while a < 3:
    print(b)
    a +=1
"""
"""
#Ül2
b = "'Tere!'"
c = '"Head aega!"'
print(b)
print("/n")
print(c)
"""
"""
#Ül 3
a = "Tere"
b = "Tore"
lause = a * 3 + "//" + b
print(lause)
"""
"""
#Ül 4
nimi = "loomariik"
print(nimi[0] + nimi[-1])
"""
"""
#Ül 5
nimi1 = "Paide"
nimi2 = "Türi"
print("Tere,"[0],nimi1[-5],nimi2,"!")
"""
"""
#Ül 6
a = "A"
b = 1
while b < 3:
    print(a,end=" ")
    b += 1
"""
"""
#Ül 7
a = 10
b = 2
print(a > b)
"""
"""
#Ül 8
a = 10
b = 2
print(a != b and b > 10)
print(b == a or a >= 0)
"""
"""
#Ül 9
from tkinter import *
raam = Tk()
raam.title("Tühi tahvel")
tahvel = Canvas(raam, width=600)

tahvel.create_rectangle(50,70,100,100, width=2, outline="blue")
tahvel.create_text(50,50, text="Tere!")

tahvel.create_polygon(100,100,150,150,200,100, fill="red",outline="black")
tahvel.pack()
raam.mainloop()
"""