s = 0
for i in range(3,1002,2):
    k = i**2
    z = i-1
    s += 4*k - 6*z
    
print(s+1)