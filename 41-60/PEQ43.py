"""
d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17

d6 must be 5 because if d6 is 0 the numbers must be of the form (011, 022, 033, ...) which are invalid
d6d7d8 it could be (506, 517, 528, 539, 561, 572, 583, 594)
d7d8d9 must be divisible by 13 therefore d6d7d8d9 has 4 possibilities (5286, 5390, 5728, 5832)
d8d9d10 must be divisible by 17 
based on the previous block of possible solutions, we can conclue that d6d7d8d9d10 can only be (52867, 53901, 57289)
for d5d6d7 can be(357, 952) since d6d7 has 3 different possibilities (52, 53, 57)
concatenating to d5d6d7d8d9d10 leaves two possible solutions, (357289, 952867)
d4 must be even and d5 either 3 or 9 and that d3d4d5 divisible by 3 all possible combinations are 
(063, 069, 123, 129, 183, 189, 243, 249, 309, 369, 423, 429, 483,
 489, 543, 549, 603, 609, 723, 729, 783, 789, 843, 849, 903, 963)

if we exclude non-pandigital we'll have 3 possibilities (30952867, 60357289, 06357289)

d1d2 = (14, 41)

d1d2d3d4d5d6d7d8d9d10 will be (1430952867, 1460357289, 1406357289, 4130952867, 4160357289, 4106357289)
"""

def subStringDivisibility():
    allPossibilities = (1430952867, 1460357289, 1406357289, 4130952867, 4160357289, 4106357289)

    return sum(allPossibilities)


print(subStringDivisibility())    


