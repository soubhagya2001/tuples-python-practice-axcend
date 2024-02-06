tuple1 = (0,1)

for i in range(2,6):
    tuple1 += (tuple1[i-1]+tuple1[i-2],)

print(tuple1)