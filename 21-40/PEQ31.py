def coinSums():
    coinSizes = (1, 2, 5, 10, 20, 50, 100, 200)
    ways = [0] * 201
    ways[0] = 1

    for i in coinSizes:
        for j in range(i, 201):
            ways[j] += ways[j - i]
        
    return ways[200]

print(coinSums())

