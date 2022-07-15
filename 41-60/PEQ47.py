from math import sqrt

def distinctPrimesFactors():
    i = 2
    upper_bound = 2 * 10 ** 5
    factor = [0] * (upper_bound)
    counter = 0
    
    while True:
        if factor[i] == 0:
            
            for j in range(2 * i, upper_bound, i):
                factor[j] += 1
                
            counter = 0
            
        elif factor[i] == 4:
            counter += 1
                
        else:
            counter = 0
            
        if counter == 4:
            return i - 3
        
        i += 1


print(distinctPrimesFactors())