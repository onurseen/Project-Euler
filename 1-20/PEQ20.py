import math

y = str(math.factorial(100))

sum = 0

for i in y:
    sum += int(i)
    
print(sum)