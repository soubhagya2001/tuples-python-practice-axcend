tuple1 = (1,2,3,4,5,6,7,8,9,10)

tuple1 = list(tuple1)
print(f"List before rotating : {tuple1}")
pos = int(input("Rotate left by : "))

for i in range(0,pos):
    tuple1.append(tuple1.pop(0))

tuple1 = tuple(tuple1)
print(f"List after rotating : {tuple1}")