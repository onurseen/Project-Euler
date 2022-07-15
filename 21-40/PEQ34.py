import math
l = []
for i in range(10**5):
    k = str(i)
    s = 0
    for j in range(len(k)):
        s += math.factorial(int(k[j]))
        if s == i:
            l.append(s)
            
print(sum(l) - 3)