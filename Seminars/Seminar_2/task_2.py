A = 6
fib1 = 1
fib2 = 1
i = 1
found = False
while fib2 < A :
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    print(fib2)
    if A == fib2 :
        found = True
        break
    i += 1
if found == True :
    print(i)
else :
    print(-1)


