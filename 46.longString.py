tuple1 = ("soubhagya","aman","akash","rohan","tapas","abdul")

maxLengthWord = tuple1[0]
maxLength = 0
for i in tuple1:
    if maxLength < len(i):
        maxLength = max(maxLength,len(i))
        maxLengthWord = i

print(f"Max length word is {maxLengthWord}")
    