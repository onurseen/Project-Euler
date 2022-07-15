import sympy as sym

x=1
 
for i in range(2,10**6):
    x += i
    if len(sym.divisors(x)) >= 500:
        print(x)
        break
    
