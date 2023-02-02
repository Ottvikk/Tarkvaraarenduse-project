"""
nimi = ['Malle', 'Volli', 'Salme', 'Kustav']
print (nimi[0])

print (nimi[2])
print (nimi[4])
print (nimi[-1])
""""""
'Tere hommikust'.split()
['Tere', 'hommikust']
'CY2X44;3;66;T'.split(';')
['CY2X44', '3', '66', 'T']
""""""
' '.join(['Tere', 'hommikust'])
'Tere hommikust'
';'.join(['CY2X44', '3', '66', 'T'])
'CY2X44;3;66;T'
""""""
for linn in ["Tartu", "Tallinn", "Põltsamaa"]:
    print("Muutuja linn väärtus: " + linn)
""""""
numbrid = [7, 5, 8, 1, 4, 5]
for nr in numbrid:
    print(nr)
""""""
a = [12, 23, 34, 45, 56]
i = 0
for el in a:
    if el > 30:
        i += 1
print(i)
"""
