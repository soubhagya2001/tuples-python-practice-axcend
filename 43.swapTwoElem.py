
tuple1 = (1, 2, 3, 4, 5)

index1 = 1
index2 = 3


list1 = list(tuple1)


list1[index1], list1[index2] = list1[index2], list1[index1]


tuple1 = tuple(list1)

print(f"Tuple after swapping elements: {tuple1}")
