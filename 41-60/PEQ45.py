"""
| Pentagonal                      							
| x = P(n)                             
| n * (3 * n - 1) / 2 = x          
| 3 * (n ** 2) - n - 2 * x = 0           
| n = (1 + (1 + 24 * x) ** 0.5) / 6      
| 1 + (1 + 24 * x) ** 0.5 % 6 ≡ 0 (mod 6) 
| (1 + 24 * x) ** 0.5 ≡ 5 (mod 6)        


T(n) = n * (n + 1) / 2 | H(n) = n * (2 * n - 1)
for n = 2 * m - 1
T(n) = (2 * m - 1) * m
for whole n = 2 * m - 1 ,that's mean n is odd, T(n) must be Hexagonal (T(n) = H(m) = T(2 * m - 1))

""" 

from math import sqrt

def isPentagonal(x):
	return sqrt(1 + 24 * x) % 6 == 5

def triangularPentagonalAndHexagonal():
	m = 144 # we know T(285) = P(165) = H(143) = 40755.

	while True:
		n = m * (2 * m - 1)

		m += 1

		if isPentagonal(n):
			return n

print(triangularPentagonalandHexagonal())