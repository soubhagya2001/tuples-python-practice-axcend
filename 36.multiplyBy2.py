tuple1 = (1,2,3,4,5)
tuple1 = list(tuple1)
for i in range(len(tuple1)):
    tuple1[i] = tuple1[i]*2

tuple1 = tuple(tuple1)
print(tuple1)