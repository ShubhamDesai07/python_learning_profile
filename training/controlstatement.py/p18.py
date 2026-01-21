'''bonus 10% to employee   yos>=5 print 10% bonus approved if yos<5 print no bonus approved 
print final salary of employee    '''



ey = int(input("Enter YOS "))
es = int(input("Enter salary"))

if ey >= 5:
    total=es+(es*0.1)
    print("10% bonus approved")
    print("total")
if ey <5:
    print ("bonus not approved")
    print("  no  ")

