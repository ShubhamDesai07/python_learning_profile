'''a = (1*1*1)+(5*5*5)+(3*3*3)
print(a)'''

n = int(input("Enter no"))
dum=n
r=0
sum=0
while n>0:
    r=n%10
    sum=sum+(r*r*r)
    n=n//10
    print(n)
if dum==sum:
    print(f"{dum}is armstrong")
else:
    print(f"{dum}is not armstrong")        