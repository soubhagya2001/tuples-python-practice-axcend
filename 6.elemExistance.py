tuple1 = (1,2,3,4,5)
num = int(input(f"Enter the number to search from the tuples {tuple1} : "))

# for i in tuple1:
#     if i == num:
#         print(f"{num} is present in the tuple {tuple1}")
#         break
    
if num in tuple1:
    print(f"{num} is present in the tuple {tuple1}")
else:
    print("Not found")