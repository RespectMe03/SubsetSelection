# Problem statement 1

import random as r

Set         = set([-12, -3, -6, 7, 2, -2, 6, 3, 9, -7, -5, -8, 1, 11, -9, -4])
SetSize     = 5
ResultList  = set()   

for i in range(1000):
    subset = r.sample(Set,SetSize)
    
    if sum(subset) == 0:
        ResultList.add(tuple(subset))

for r in ResultList:
    print(r)

print("\n Total Sets: ", len(ResultList))


# 2nd Problem
# Constraint: Subset size must be 3 to 6 only

import random as r

Set         = set([-12, -3, -6, 7, 2, -2, 6, 3, 9, -7, -5, -8, 1, 11, -9, -4])
LB = 3
UB = 6
ResultList  = set()   

for i in range(1000):
    SetSize = r.randint(LB,UB)

    subset = r.sample(Set,SetSize)
    if sum(subset) == 0:
        ResultList.add(tuple(subset))

for r in ResultList:
    print(r)

print("\n Total sets: ", len(ResultList))