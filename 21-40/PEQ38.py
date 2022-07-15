"""
First of all the number must be less than 5 digits, more than 3 digits, that is, it must be 4 digits
The number has start with 9 and second digit must be less than 5 and number cannot contain 1
then it must be
9234 <= x <= 9487
"""

def isPandigital(x):
    controlNumber = set('123456789')
    control = ''

    for n in range(1, 3):
        control += str(n * x)
        
    if controlNumber == set(control):
        return int(control) # control > 0 equals to True
    
    return False
        
def pandigitalMultiples():
    result = 0
    
    for i in range(9234, 9488):
        temp = isPandigital(i)
        if temp and temp > result:
            result = temp
            
    return result

print(pandigitalMultiples())

