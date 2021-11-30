#Find factors
import math

def factors(num):
    factor = []
    for i in range(1, int(math.floor(num**0.5)) + 1):
        if num % i == 0:
            factor.append(i)
            factor.append(num // i)
    return factor
    

#Check for largest prime



def largestprime(num):
    return len(factors(num)) == 2

reallargestfacttor = 0
allfactors = factors(600851475143)
for j in allfactors:
    if largestprime(j) and j > reallargestfacttor:
        reallargestfacttor = j


print reallargestfacttor



largestprime(12)







