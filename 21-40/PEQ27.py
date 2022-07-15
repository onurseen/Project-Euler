def prime(x):
    l1,l2 , sieves = [], [], ([True]*x)
    for i in range(2,x):
        if sieves[i]:
            l1.append(i)
            l2.append(-i)
            for j in range(i*i,x,i):
                sieves[j] = False
    n = l2 + l1
    n.sort()
    return n

def isprime(x):
    for i in range(2,int(abs(x)**0.5)+1):
        if x % i == 0:
            return False
    return True
b = prime(1000)

MaxA, MaxB, MaxN = 0,0,0
for i in range(-999,1000,2):
    for j in range(len(b)):
        for k in range(2): 
            n = 0
            cntrl = 1 if k == 0  else -1
            iodd = -1 if j % 2 == 0 else 0

            while isprime(n * n + (i + iodd) * n + cntrl * b[j]):
                n += 1

            if n > MaxN:
                MaxA, MaxB, MaxN = i, b[j], n
            
print(MaxA*MaxB,MaxN)
