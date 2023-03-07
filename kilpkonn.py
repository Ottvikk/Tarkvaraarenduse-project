import turtle #impordib turtle

pcolor = ("black")
kilpkonna_juhised = [] #loob järjendi

f = open('kilpkonn.txt','r') #avab tekstidokumendi juhistega
print(f.read()) #loeb neid juhiseid
for rida in f:
    kilpkonna_juhised.append(rida.strip)

# tõlgib eestikeelsed juhendid turtleile arusaadavaks
def joonista_kujund(kujund, kilpkonn):
    for käsk in kujund:
        if käsk[0] == "edasi":
            kilpkonn.forward(int(käsk[1]))
        elif käsk[0] == "tagasi":
            kilpkonn.backward(int(käsk[1]))
        elif käsk[0] == "paremale":
            kilpkonn.right(int(käsk[1]))
        elif käsk[0] == "vasakule":
            kilpkonn.left(int(käsk[1]))


print(kilpkonna_juhised) #väljastab konsooli juhised

turtle.exitonclick() #sulgeb mängu ekraanile vajutades