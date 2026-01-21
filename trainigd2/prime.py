#

n = int(input("Enter no"))
i = 2 
flag = True
while i<=n/2:
    if n%i==0:
        flag = False
        break
    i = i+1
if flag:
    print(f"{n}is prime")
else:
    print(f"{n}is not prime ")        