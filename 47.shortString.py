tuple1 = ("soubhagya","aman","akash","rohan","tapas","abdul")

minLengthWord = tuple1[0]
minLength = len(tuple1[0])
for i in tuple1:
    if minLength > len(i):
        minLength = min(minLength,len(i))
        minLengthWord = i

print(f"Max length word is {minLengthWord}")
    