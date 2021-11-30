
sumofsquares = 0 

for i in range(1,101):
    sumofsquares = sumofsquares + i ** 2


sums = 0
for j in range(1,101):
    sums = sums + j 

squareofsums = sums ** 2

answer = sumofsquares - squareofsums

print(answer)

