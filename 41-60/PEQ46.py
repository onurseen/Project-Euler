"""
x = p + 2 * q ** 2
x is a odd composite number, p and q are a prime numbers

"""

from math import sqrt

def isPrime(x):
	if x % 2 == 0:
		return False

	for i in range(3, int(sqrt(x)) + 1, 2):
		if x % i == 0:
			return False

	return True

def isSquare(x):
	control = pow(x, 0.5)

	return control == int(control)

def goldbachControl(x):
	for i in range(1, x, 2):
		if isSquare((x - 2) / 2) or (isPrime(i) and isSquare((x - i) / 2)):
			return False
			
	return True

def GoldbachsOtherConjecture():
	x = 7

	while True:
		x += 2

		if isPrime(x):
			continue

		if goldbachControl(x):
			return x
		
print(GoldbachsOtherConjecture())
