a = [i for i in range(2,101)]

i = 0
j = 0
n = len(a)
l = []

while True:
    l.append(a[i]**a[j])
    
    j += 1
    
    if j == n:
        i += 1
        j = 0
    if i == n:
        break
        
l.sort()
print(len(set(l)))
