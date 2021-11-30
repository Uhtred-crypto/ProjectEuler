import math
from typing import final 

def checkprime(num):
    prime_flag = 0
    for i in range(2, int(math.floor(num**0.5) + 1)):
        if num % i == 0:
            prime_flag = 1
            break
    if prime_flag == 0:
        return True
    else:
        return False

        


result = []
for j in range (3, 2000000, 2):
    if checkprime(j) == True:
        result.append(j)

finalresult = 2
for l in result:
    finalresult = finalresult + l
print(finalresult)






