from math import sqrt

def abundantNums():
    abundants = []
    
    for i in range(12, 28123):
        factor = 1
        for j in range(2, int(sqrt(i)) + 1):
            if i % j == 0:
                factor += j + i//j
                if j == sqrt(i):
                    factor -= j
        if factor > i:
            abundants.append(i)
            
    cntrl = [True] * 28124
    x = 0
    for _ in abundants:
        for __ in abundants[x:]:
            if _ + __ > 28123: break
            cntrl[_ + __] = False
        x += 1
        
    sum = 0
    for t in range(1, 28123):
        if cntrl[t]:
            sum += t
            
    return sum
            

print(abundantNums())
