tuple1 = (1,2,3,4,5)
num = int(input(f"Enter the number to search from the tuples {tuple1} : "))

for i in range(len(tuple1)):
    if tuple1[i] == num:
        print(f"Found {num} in index {num}")
        break