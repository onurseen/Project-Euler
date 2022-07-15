l = [1,1]

for i in range(10**6):
    l.append(l[i]+l[i+1])
    if len(str(l[-1])) >= 1000:
        print(l.index(l[-1])+1)
        break