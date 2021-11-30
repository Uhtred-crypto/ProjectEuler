values = [1,2,3]

for i in range(1,1000000):
  values.append(values[len(values) - 1] + values[len(values) - 2])
  if values[len(values) - 1] >= 4000000:
      break
  
evenvalues = []

for j in values:
    if j % 2 == 0:
        evenvalues.append(j)

finalvalue = 0

for l in evenvalues:
    finalvalue = finalvalue + l

print(finalvalue)
    
