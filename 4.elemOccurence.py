tuple1 = (1,2,3,4,5,4,2,6)
numToFind = 2
noOfOccurence = 0
for i in tuple1:
    if i == numToFind:
        noOfOccurence +=1

print(f"Number of occurence of {numToFind} is {noOfOccurence}")