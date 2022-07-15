n=1000
maxA = n // 3
for i in range(1, maxA):
    for j in range(i+1,(n-i)//2):
        c = n-i-j
        if i < j and j < c and i**2 + j**2 == c**2:
            print(i*j*c)