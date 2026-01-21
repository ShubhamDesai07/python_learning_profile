n = int(input("Enter no"))
dum=n
r=0
sum=0
while n>0:
    r=n%10
    sum=(sum*10)+r
    n=n//10
    print(n)
if dum==sum:
    print(f"{dum}is palindrome")
else:
    print(f"{dum}is not palindrome")        