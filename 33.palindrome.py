tuple1 = (1,2,3,4,5,3,2,1)
start = 0
end = len(tuple1)-1

isPalindrome = True
while(start<end):
    if(tuple1[start] != tuple1[end]):
        isPalindrome = False
    
    start +=1
    end -= 1

if(isPalindrome):
    print(f"{tuple1} is a palindrome")
else:
    print(f"{tuple1} is not a palindrome")
    
