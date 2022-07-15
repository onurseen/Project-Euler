x1,x2 = 0,0
for i in range(1,101):
    x1 += i
    x2 += i**2
    
print(x1**2-x2)