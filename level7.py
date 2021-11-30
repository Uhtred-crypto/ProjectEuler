import math 

tempprime = []
prime = []


#check if number is pime
def factors(num):
    tempprime.clear()
    for i in range(1, int(math.floor(num ** 0.5) + 1)):
        if num % i == 0:
            tempprime.append(i)
    if len(tempprime) <= 1:
        return True

j = 2

while len(prime) < 10001:
    if factors(j) == True:
        prime.append(j)
    j = j + 1


print(prime[len(prime) - 1])

            
            