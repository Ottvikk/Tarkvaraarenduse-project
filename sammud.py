"""
f = open('sammud.txt')

kogus = 0
while True:
    nimi = f.readline()
    print(nimi)
    if nimi == "":
        break

print(len(nimi))
print(kogus)

f.close()
"""
"""
myfile = 'sammud.txt'
sum = 0
a = 0
with open(myfile) as fh:
    for n in fh:
        n = n.strip()
        sum = sum + int(n)
        a = a + 1
        sum1 = sum / a
print('Päevade peale oli samme kokku ' + str(sum))
print('Kokku liikusid ' + str(a) + ' Päeva')
print('Päeva keskmine sammude arv on ' + str(sum1))
"""
b = open('sammud.txt', 'r')

c = b.readlines()
regels = len(c)

print(regels)

max = 0
for line in b.readlines():
  num = int(line.split(",")[0])
  if (max < num):
    max = num


print(max)
# Close file
b.close()