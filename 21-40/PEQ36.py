sum = 0
for i in range(10**6):
    x = bin(i)[2:]
    if str(i) == str(i)[::-1] and x == x[::-1]:
        sum += i
print(sum)
        