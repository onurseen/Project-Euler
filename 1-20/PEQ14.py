def collatz(chain, x):
    if not chain.get(x, 0):
        if x % 2: chain[x] = 1 + collatz(chain, 3*x + 1)
        else: chain[x] = 1 + collatz(chain, x/2)
    return chain[x]
chain = {1: 1}

a, b = 0, 0
for i in range(1, 10**6):
    c = collatz(chain, i)
    if c > a: a, b = c, i
        
print(b)