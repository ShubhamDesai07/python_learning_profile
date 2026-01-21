#fibonacci series

'''start
declare n,i,ft,st,tt
initilize i=1 ft=0 st=1
read n
print ft,st
repeat the stages until i<=n-2
    tt=ft+st
    display tt
    ft=st
    st=tt
    i=i+1
dry run
n i ft st tt
5 1 0  1   1
  2 1  1   2
  3 1  2   3
  4 2  3                 '''




n = int(input("Enter n "))
i = 1
ft = 0 
st = 1 
tt = 0
print (f"{ft} {st}")
while i<=n-2:
    tt = ft+st
    print(f"{tt}")
    ft = st
    st = tt
    i = i+1  
