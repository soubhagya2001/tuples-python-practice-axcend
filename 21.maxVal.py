tuple1 = (12,4,5,67,21)
maxVal = tuple1[0]

for i in tuple1:
    maxVal = max(maxVal,i)

print(f"Maximum value in {tuple1} is {maxVal}")