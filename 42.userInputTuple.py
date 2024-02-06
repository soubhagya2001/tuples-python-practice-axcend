tuple1 = ()
numOfInput = int(input("How much number of words do you want to insert : "))

for i in range(numOfInput):
    num = int(input("Insert Data : "))
    tuple1 += (num,)


print(tuple1)