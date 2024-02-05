tuple1 = ((1,2,3),(4,5,6),(7,8,9))

tuple2 = ()

for i in tuple1:
    for j in i:
        tuple2 += (int(j),)

print(tuple2)