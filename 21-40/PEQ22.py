with open('names.txt', 'r') as names:
    x = names.read()
    sortedNames = sorted(x.replace('"','').split(','), key=str)
    
sum = 0

for loc, val in enumerate(sortedNames):
    counter = 0
    for i in val:
        counter += ord(i) - 64
    sum += counter * (loc + 1)
    
print(sum)