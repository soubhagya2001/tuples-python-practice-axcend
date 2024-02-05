tuple1 = (1,27,3,4,5)

isSorted = True
for i in range(len(tuple1)-2):
    if(tuple1[i] > tuple1[i+1]):
        isSorted = False
    
if(isSorted):
    print(f"{tuple1} is sorted")
else:
    print(f"{tuple1} is not sorted")