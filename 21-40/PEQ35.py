def primes(x):
    l , sieves = set(), ([True] * x)
    
    for i in range(2, x):
        if sieves[i]:
            for j in range(i*i, x, i):
                sieves[j] = False
                
            i = str(i)
            
            if '2' in i or '4' in i or '5' in i or '6' in i or '8' in i or '0' in i:
                continue
            
            l.add(i)                
    return l

def rotation(x):
    s = set()
    
    for i in range(len(x)):
        temp = x[i:] + x[:i]
        s.add(temp)
    
    return s

def circularPrimes():
    wp = primes(10**6)
    circularPrimes = {2, 5}
    
    for i in wp:
        if i in circularPrimes:
            continue
        x = rotation(i)
            
        if x.issubset(wp):
            circularPrimes.update(x)
            
    return circularPrimes

 
print(len(circularPrimes()))
