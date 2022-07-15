def fifth(k):
    n = int(k)
    return n ** 5


temp = 0

for i in range(2,2*10**5):
    if sum(list(map(fifth, list(str(i))))) == i:
        temp += i

print(temp)