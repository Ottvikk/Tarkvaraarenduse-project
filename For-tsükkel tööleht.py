"""
Linnad = ["Tartu", "Võru", "Valga", "Viljandi", "Narva", "Pärnu", "Tallinn"] #Järjend
linn = sorted(Linnad) #defineerib sõna linn
print(linn) #prindib sõna linn
x = len(Linnad)
print("Järjendis on " + str(x) + " linna.") #Prindib lause järjendis on siis järjendis olev lause ja linn lõppu
"""
"""
a =[2,3,1,5] # Andmed järjendis
b =[6,4]
c = a + b  #C on järjendi a ja b kokku liitmine
d = sorted(c) #D on c aga ära sorteerituna
print(d) #Prindib d
"""
"""
Linnad = ["Tartu", "Võru", "Valga", "Viljandi", "Narva", "Pärnu", "Tallinn"] #Järjend
for a in range(0, 7, 1): #Tsükkel mis paneb järjendis teksti lugema kindlas järjekorras
    print(Linnad[a]) #Prindib linnad kindlas järjekorras
"""
"""
import turtle #Impordib turtle

for i in range(4): #Loeb all olevat teksti nelikorda ja joonistab selle järgi
   turtle.forward(50)
   turtle.right(90)
turtle.done() #Sellega saab programm läbi
"""
"""
n = int(input("Mitu numbrit sa tahad sisestada?: ")) #Küsib kasutajalt mitu nubrit sa tahad sisestada
total_sum = 0 #Lõpplik summa

for i in range(n): # For tsükkel
    # 'x += y' on sama mis  x = x+y
    total_sum += int(input())#Liidab kokku numbrid mis sisestati.
print(total_sum)
"""
"""
for i in [2,3,4,4]: #For tsükkel
    if (i%2) == 0: #Jagatakse järjendis olevaid numbreid 2-ga
        print("Paaris arv") #Kui jagub 2-ga siis prindib välja paaris arv
    else:
        print("Paaritu arv")#Kui ei jagu 2-ga siis prindib välja paaritu arv
"""
"""
print("Sisesta kuupäev näiteks nagu 10.02.1990") #Prindib välja näite kuidas sisestada kuupäeva
aeg = [] #Tühi järjend
aeg = input(str("Sisesta päev, kuu ja aasta: "))  #Küsib kasutajalt päeva, kuupäeva ja aastat

print(aeg)#Prindib järjendi
aeg1 = aeg.split('.')#Lõhub järjendi ära mitmeks osaks
print(aeg1)#Prindib järjendi
print(str(aeg1[1]))#Prindib järjendi osad ühekaupa
print(str(aeg1[0]))
print(str(aeg1[2]))

if aeg1[1] == '01':Kui kasutaja kirjutab kuu numbritega siis see muudab numbri tähtedeks 
    a = 'jaanuar'
    print(a)
elif aeg[1] == '02':
    a = 'veebruar'
    print(a)
elif aeg1[1] == '03':
    a = 'märts'
    print(a)
elif aeg[1] == '04':
    a = 'aprill'
    print(a)
elif aeg1[1] == '05':
    a = 'mai'
    print(a)
elif aeg[1] == '06':
    a = 'juuni'
    print(a)
elif aeg1[1] == '07':
    a = 'juuli'
    print(a)
elif aeg[1] == '08':
    a = 'august'
    print(a)
elif aeg1[1] == '09':
    a = 'september'
    print(a)
elif aeg[1] == '10':
    a = 'oktoober'
    print(a)
elif aeg1[1] == '11':
    a = 'november'
    print(a)
else:
    aeg[1] == '12'
    a = 'detsember'
    print(a)

print(aeg1[0] + '.' + a + ' ' + aeg1[2]) #Prindib kasutajale kuupäeva
"""






