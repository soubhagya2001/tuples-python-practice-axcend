tuple1 = (1,2,3,4,5)
tuple2 = ()

for i in tuple1:
    tuple2 += (str(i),)

print(tuple2)