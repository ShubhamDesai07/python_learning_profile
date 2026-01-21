''' 1 male workers 5% bonus on salary
2 female 10% bonus on salary
if salary <10000 then print additional 2% as bonus'''

ms = int(input("Enter salary"))
fs = int(input("Enter salary"))

if ms<10000:
    t = ms+(ms*0.07) 
    print("7% bonus")
    print(t)
else:
    t = ms+(ms*0.05)
    print("5% bonus")     
    print (t)
