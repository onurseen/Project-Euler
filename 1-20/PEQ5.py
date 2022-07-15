def gcd(a,b):  # gcd = lambda a,b: b and gcd(b, a % b) or a
    if b == 0:
        return a
    return gcd(b, a%b)

def lcm(a,b): # lcm = lambda a,b: a * b / gcd(a,b)
    return a * b / gcd(a, b)

n = 1
for i in range(1, 21):
    n = lcm(n, i)

print(n)
