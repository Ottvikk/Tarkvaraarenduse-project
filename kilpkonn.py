import turtle #impordib turtle

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

pcolor = ("black")
kilpkonna_juhised = [] #loob järjendi

f = open('kilpkonn.txt','r') #avab tekstidokumendi juhistega
print(f.read()) #loeb neid juhiseid
for rida in f:
    kilpkonna_juhised.append(rida.strip)
def turtle(self,draw,starts):
    self.turtle = turtle
    self.draw = draw
    self.starts = starts
    def drawing(self):
        self.draw(starts)
        if starts == True:
            turtle.begin_fill(black)



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


                    print(joonista_kujund) #väljastab konsooli juhised

                    turtle.exitonclick()#sulgeb mängu ekraanile vajutades
                    pygame.quit()