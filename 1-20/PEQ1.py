print(sum([i for i in range(1000) if i % 15 == 0 ] + [i for i in range(1000) if (i % 3 == 0 or i % 5 == 0) and i % 15 != 0 ]))