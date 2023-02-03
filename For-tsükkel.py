"""
list(range(5))
[0, 1, 2, 3, 4]
list(range(0, 5))
[0, 1, 2, 3, 4]
list(range(2, 5))
[2, 3, 4]
list(range(0, 15, 2))
[0, 2, 4, 6, 8, 10, 12, 14]
list(range(5, 0, -1))
[5, 4, 3, 2, 1]
""""""
for i in range(5):
    print(i)
""""""
arvud = [2,4,6,7,2]
for i in range(0,5,1):
    print(arvud[i])
""""""
a = []
a.append(2)
""""""
a = [2,3,4]
a[2] = 90
a[elemendi_indeks] = uus_väärtus
"""
f = open('test.txt')
for rida in f:
    print('Lugesin järgneva rea: ' + rida)
f.close()
"""
f = open('nimed.txt')
while True:
    nimi = f.readline() # loeb failist ühe rea
    # kui jõuti faili lõppu, siis readline tagastab tühja sõne
    if nimi == "":
        break

f.close()
""""""
nimekiri = []
f = open('nimekiri_10it.txt',encoding='utf-8')
for rida in f:
    nimekiri.append(rida.strip())
f.close()
suvaline = random.randint(0,len(nimekiri)- 1)
print(nimekiri[suvaline])
"""

