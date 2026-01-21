global flag
def prime(n):
    i=2
    flag=True

    while i<=n//2:

        if n%i==0:
            flag=False
            break
        i+=1
        return flag
n = int(input("Enter a number")) 
flag=prime(n)
print(flag)
if flag:
    print(f"{n}is prime")
else:
    print(f"{n}is not prime")    
