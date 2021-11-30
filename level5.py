def check(num):
    if num % 20 == 0:
        if num % 19 == 0:
             if num % 18 == 0:
                if num % 17 == 0:
                    if num % 16 == 0:
                        if num % 15 == 0:
                            if num % 14 == 0:
                                if num % 13 == 0:
                                    if num % 12 == 0:
                                        if num % 11 == 0:
                                            if num % 7 == 0:
                                                if num % 3 == 0:
                                                    return True
        
    
answer = []

for i in range (20, 1000000000000, 20):
    if check(i) == True:
        answer.append(i)


print(answer)


