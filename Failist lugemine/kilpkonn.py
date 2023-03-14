import turtle

a = input("Sisestage programmi pealkiri: ") #Paneb pealkirja
turtle.title(a)
kord = int(input("Mitu korda kujund joonistada? :  ")) #Küsib kasutajalt mitu korda joonistatakse seda kujundit

def instructions(turtle): #Defineerib sõna instructions
    juhend = []
    with open(turtle, 'r') as f: #Avab teksti faili
        for rida in f:
            command = rida.strip().split(' ') #Poolitab faili
            juhend.append(command)
    return juhend

def draw_shape(ruut, turtle): #Joonistab ruudu
    for command in ruut:
        if command[0] == 'edasi':
            turtle.forward(int(command[1]))
        elif command[0] == 'tagasi':
            turtle.backward(int(command[1]))
        elif command[0] == 'paremale':
            turtle.right(int(command[1]))
        elif command[0] == 'vasakule':
            turtle.left(int(command[1]))

juhend = instructions('kilpkonn.txt') #Võtab juhendi

turtil = turtle.Turtle()
turtil.hideturtle()
turtil.speed(0)

for i in range(kord): #Hakkab joonistama
    draw_shape(juhend, turtle)

turtle.exitonclick()