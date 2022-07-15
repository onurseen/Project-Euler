from itertools import permutations 

def turn(k):
    s = ''
    for i in k:
        s += i
    return int(s)


k = list(map(turn, permutations("0123456789")))
k.sort()

print(k[10**6-1])
