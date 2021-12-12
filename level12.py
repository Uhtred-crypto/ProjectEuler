import math
answer = False
start = 1
add = 2



while answer == False:
    start = start + add
    factors = []
    for i in range(1, math.floor(math.sqrt(start))):
        if start % i == 0:
            factors.append(i)
    if len(factors) > 250:
        answer = True
    add += 1
       
print(start)


