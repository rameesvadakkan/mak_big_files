myset = {1,4,6,9}
myset2 = {5,6,9,1}

myset3 = myset.union(myset2)

print(myset3)

myset4 = myset.intersection(myset2)
print(myset4)

myset5 = myset & myset2

print(myset5)

myset.intersection_update(myset2)

print(myset)

myset6 = myset.difference(myset2)

print(myset6)