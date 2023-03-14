
sammud = 'sammud.txt'
sum = 0
a = 0
with open(sammud) as fh:
    for n in fh:
        n = n.strip()
        sum = sum + int(n)
        a = a + 1
        sum1 = sum / a
print('Päevade peale oli samme kokku ' + str(sum))
print('Kokku liikusid ' + str(a) + ' Päeva')
print('Päeva keskmine sammude arv on ' + str(sum1))


ln = 0
maxln = 0
maxn = 0
with open('sammud.txt', 'r') as f:
    line = f.__next__()
    if line:
       ln = 1
       maxln = 1
       maxn = int(line.split(",")[0].strip())
    else:
       raise Exception('Empty content')
    for line in f:
        ln += 1
        cur = int(line.split(",")[0].strip())
        if cur > maxn:
            maxn = cur
            maxln = ln
print (str(maxln) + ' päeval oli sammude arv suurim')
print ('Suurim sammude arv oli ' + str(maxn)) #result


ln = 0
lowln = 0
lown = 0
with open('sammud.txt', 'r') as f:
    line = f.__next__()
    if line:
       ln = 1
       lowln = 1
       lown = int(line.split(",")[0].strip())
    else:
       raise Exception('Empty content')
    for line in f:
        ln += 1
        cur = int(line.split(",")[0].strip())
        if cur < lown:
            lown = cur
            lowln = ln
print (str(lowln) + ' päeval oli sammude arv väikseim')
print ('Väikseim sammude arv oli ' + str(lown)) #result

