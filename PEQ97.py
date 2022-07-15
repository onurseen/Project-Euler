def pows(x, y, z, k):
    return (z * pow(x, y, k) + 1) % k

print(pows(2, 7830457, 28433, 10**10))