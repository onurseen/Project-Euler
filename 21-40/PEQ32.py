main = set()
control = set('123456789')

for i in range(9):
    for j in range(999, 9999):
        k = str(i) + str(j) + str(i*j)
        
        if len(k) == 9 and set(k) == control:
            main.add(i*j)
        if len(k) > 9: 
            break
        
for i in range(9, 99):
    for j in range(99, 999):
        k = str(i) + str(j) + str(i*j)
        
        if len(k) == 9 and set(k) == control:
            main.add(i*j)
        if len(k) > 9: 
            break
         
print(sum(main))