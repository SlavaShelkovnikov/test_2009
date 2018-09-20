number = int(input())
finalNumber = number
simpleNumber = 2
counter = 0
a = []
while simpleNumber <= number:
    while number % simpleNumber == 0:
        number = number // simpleNumber
        counter += 1
    for i in range(counter):
        a.append(simpleNumber)
    simpleNumber += 1
    counter = 0
print(finalNumber, '=', a[0], sep='', end='')
for x in a[1:len(a)]:
    print('*', x, sep='', end='',)
