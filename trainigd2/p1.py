'''m1 m2 m3 atte of 3 students 
if att>or = 90% add extra 5% do stu Per
if stu plays a sport add an extra 2% to the students Per
check the per if per>=40 print pass per<40 print fail    '''

m1 = int(input("Enter m1 marks"))
m2 = int(input("Enter m2 marks"))
m3 = int(input("Enter m3 price"))
at = int(input("Enter attendence1"))
sp = str(input("Plays sports yes or no"))

t = m1+m2+m3
per = (t/300)*100
print ("total mark",t)
#y = yes
#n = no
if at>=90:
    print("your percentage is ",per+0.05)
elif sp==y:
    print("your percentage in sports ",per+0.02)

elif sp==n:
    print("your percentage is ",per)        
