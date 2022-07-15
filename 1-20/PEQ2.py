l = [1,1]
sum = 0
for i in range(50):
    l.append(l[i]+l[i+1])
    if l[i] % 2 == 0:
        if l[i] > 4*10**6:
            break
        sum += l[i]
print(sum)