def reciprocalCycles():
    longestNum = lenght = 1 
    
    for i in range(3, 1000, 2):
        if i % 5 == 0:
            continue
        
        x = 1
        
        while (10 ** x) % i != 1:
            x += 1
            
        if x > lenght:
            longestNum, lenght = i, x
            
    return longestNum

print(reciprocalCycles())