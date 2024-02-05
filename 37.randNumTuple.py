import random

tuple1 = ()
for i in range(10):
    tuple1 += (random.randint(0,100),)

print(tuple1)