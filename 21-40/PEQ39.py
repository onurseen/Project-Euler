"""
a + b + c = p
a**2 + b**2 = c**2
a <= b < c
a < p / 3

if a is odd b is even c becomes odd and a + b + c = p becomes even
also if a is even b is odd c becomes odd and a + b + c = p becomes even
finally if a is even and b is even c becomes even and a + b + c = p becomes even
in all cases p is even

if a = 0; 
0 + b + c <= p
b**2 = c**2
b = c
b + c <= 1000
b <= 500

a**2 + b**2 = (p - a - b)**2 = p**2 + a**2 + b**2 - 2pa - 2pb + 2ba
2pb - 2ba = p**2 - 2pa
2b(p-a) = p(p - 2a)
b = p(p - 2a)/2(p - a)
"""

def integerRightTriangles():
    temp = max = 0
    
    for p in range(2, 1001, 2):
        counter = 0
        for a in range(2, p//3):
            if ((p * (p - 2 * a)) % (2 * (p - a))) == 0:
                counter += 1
                
        if counter > temp:
            temp = counter
            max = p
            
    return max

print(integerRightTriangles())