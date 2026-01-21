'''given a postive int num reduce it to a palindrome by performing following steps 
if num is palindrome , reverse its digits and add it to original number

repeat until the number becomes a palindorme or you have done 1000 iterations 

return the resulting palindrome or -1 if not found within 1000 steps 

example input :
num = 87
output = 4884 
 explanation :87+78=165,                           '''

num = int(input("Enter no"))
steps = 0

while steps <1000:
    if str(num) == str(num)[::-1]:
        break
    rev = int(str(num)[::-1])
    num = num + rev 
    steps += 1
    print(num)
    
if str(num) == str(num)[::-1]:
    print(f"Palindrome found: {num}")
else:
    print(-1) 


    
       