f = open('kilpkonn.txt')
import turtle
korrad = input("Sisesta mitu korda tegema peab: ")
while True:
    nimi = f.readline()
    print(nimi)
    if nimi == "":
        break


f.close()