"""
1 <= x < y <= 9
1 <= z <= 9
x/y < 1 
we have 4 possibilities and three of them have no solution
(10*z + x) / (10*z + y) = x / y #no solution
(10*z + x) / (10*y + z) = x / y #no solution
(10*x + z) / (10*y + z) = x / y #no solution
(10*x + z) / (10*z + y) = x / y #have solution
"""
from math import gcd

def	digitCancellingFractions():
    a = b = 1

    for z in range(1, 10):
        for y in range(1, z):
            for x in range(1, y):
                if (x*10 + z) * y == (z*10 + y) * x:
                    a *= y
                    b *= x
                
    return a // gcd(a, b)
              
print(digitCancellingFractions())