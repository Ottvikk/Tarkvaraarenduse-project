f = open('kilpkonn.txt')
from turtle import *
korrad = input("Sisesta mitu korda tegema peab: ")
while True:
    for i in range(int(korrad)):
       turtle = turtle.square(100)
    nimi = f.readline()
    print('turtle.' + nimi)

    if nimi == "":
        break

f.close()