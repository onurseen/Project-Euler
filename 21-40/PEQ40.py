x = ''
for i in range(1,200000):
    x += str(i)
    
k = int(x[0])*int(x[9])*int(x[99])*int(x[10**3-1])*int(x[10**4-1])*int(x[10**5-1])*int(x[10**6-1])

print(k)
