f = open('kilpkonn.txt')
import turtle

while True:
    nimi = f.readline()
    print(nimi)
    if nimi == "":
        break


f.close()