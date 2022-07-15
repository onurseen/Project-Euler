def prime(x):
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

i = 0
j = 2
while True:
    if prime(j):
        i += 1
    if i == 10001:
        print(j)
        break
    j += 1   