factors = []

for i in range(888888, 999999, 11):
    if i % 11 == 0:
        factors.append(i)


def findpalindrom(num):
    x = str(num)
    y = ""
    for i in x:
       y = i + y
    return int(y) == num

palindromes = []

for l in factors:
    if findpalindrom(l) == True:
        palindromes.append(l)


highestPal = 0

for x in range (999, 100, -1):
    for y in range (999, 100, -1):
        temp = x * y
        if temp in palindromes:
            if temp > highestPal:
                highestPal = temp

print(highestPal)
            






























