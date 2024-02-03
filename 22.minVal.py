tuple1 = (12,4,5,67,21)
minVal = tuple1[0]

for i in tuple1:
    minVal = min(minVal,i)

print(f"Minimum value in {tuple1} is {minVal}")