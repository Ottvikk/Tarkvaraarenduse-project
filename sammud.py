f = open('sammud.txt')

kogus = []
while True:
    nimi = f.readline()
    print(nimi)
    if nimi == "":
        break

print(len(nimi))
print(kogus)

f.close()