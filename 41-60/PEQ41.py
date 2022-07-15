"""
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45 it's cannot become a prime because it divisible by three 
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 = 36 and the same reason it's cannot
1 + 2 + 3 + 4 + 5 + 6 + 7 = 28 it's can be prime and 
therefore the largest pandigital number has at most 7 digits and as such is 7654321
"""

from itertools import permutations

def isPrime(x):
    if x % 2 == 0 and x != 2:
        return False

    for i in range(3, int(x ** 0.5), 2):
        if x % i == 0:
            return False

    return True

def numb(x):
    n = ''

    for i in range(len(x)):
        n += str(x[i])

    return int(n)

def pandigitalPrime():
    for i in permutations(range(7, 0, -1)):
        temp = numb(i)

        if isPrime(temp):
            print(temp)
            break

print(pandigitalPrime())