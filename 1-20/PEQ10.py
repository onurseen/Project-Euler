def primes(x):
    temp, sieves = [], ([True]*x)
    for i in range(2, x):
        if sieves[i]:
            temp.append(i)
            for j in range(i*i, x, i):
                sieves[j] = False
    return temp

print(sum(primes(2000000))) 