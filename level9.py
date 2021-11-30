
triplets = []

a = []
b = []
c = []
result = []


for i in range(1, 1000):
    if i % 3 == 0:
        a.append(i)

for j in range(1, 1000):
    if j % 4 == 0:
        b.append(j)

for k in range(1, 1000):
    if k % 5 == 0:
        c.append(k)



for num1 in a:
    for num2 in b:
        for num3 in c:
            if num1 + num2 + num3 == 1000 and num1**2 + num2**2 == num3**2:
                result.append([num1, num2, num3])
    
    
finalresult = 1

for l in result[0]:
    finalresult = finalresult * l

print(finalresult)







