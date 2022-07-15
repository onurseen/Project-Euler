"""
x = P(n)
n * (3 * n - 1) / 2 = x
3 * (n ** 2) - n - 2 * x = 0
n = (1 + (1 + 24 * x) ** 0.5) / 6
1 + (1 + 24 * x) ** 0.5 % 6 ≡ 0 (mod 6)
(1 + 24 * x) ** 0.5 ≡ 5 (mod 6)

P(x + 1) = P(x) + 3 * x + 1
"""

from math import sqrt

def isPentagonal(x):
	return sqrt(1 + 24 * x) % 6 == 5

def pentagonNumbers():
	x = 1
	P_x = 1
	pentagonalNums = [1]

	while True:
		x += 3
		P_x += x
		pentagonalNums.append(P_x)

		for i in range(len(pentagonalNums)):
			P_i = pentagonalNums[i]
			P_n = P_x - P_i
 		
			if P_n - P_i < 0:
				break

			if isPentagonal(P_n) and isPentagonal(P_n - P_i):
				return P_n - P_i

print(pentagonNumbers())


