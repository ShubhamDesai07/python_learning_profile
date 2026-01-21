def armsrtong(n):
    r=0
    sum=0

    while n>0:
        r=n%10
        sum+=r**3
        n=n//10
    return sum
n=int(input("Enter a number"))  
sum=armsrtong(n)
if sum==n:
    print(f"{n} is armstrong")  
else:
    print(f"{n} is not armstrong")    