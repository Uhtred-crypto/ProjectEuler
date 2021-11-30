multiples = []

for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        if i not in multiples:
            multiples.append(i)

finalvalue = 0

for j in multiples:
    finalvalue = finalvalue + j

print(finalvalue)

