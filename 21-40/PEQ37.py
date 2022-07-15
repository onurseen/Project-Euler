from math import sqrt
from time import time

start = time()

def isPrime(x):
    if x == 1:
        return False
    
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
        
    return True

def truncatablePrimes():
    counter = sums = 0
    x = 9
    
    while counter < 11:
        x += 2
        i = str(x)
        
        if ('0' in i or '2' in i or '4' in i or '5' in i or '6' in i or '8' in i) and len(i) != 2:
            continue
        
        if isPrime(x):
            flag = 0
            
            for k in range(len(i)):
                if not isPrime(int(i[k:])) or not isPrime(int(i[:len(i) - k])):
                    flag = 1
                    break
                
            if flag == 0:
                sums += x 
                counter += 1               
            
    return sums

print(truncatablePrimes(), time() - start)
