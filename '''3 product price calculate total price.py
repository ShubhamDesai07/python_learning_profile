'''3 product price calculate total prices  total<500 then give 10per discount of total price 
if total=500 then give 30per discount 
print total price 
how much discount 
discount amount 
final amount'''

p1 = int(input("Enter p1 price"))
p2 = int(input("Enter p2 price"))
p3 = int(input("Enter p3 price"))

sum = p1+p2+p3
print(sum)

if sum >= 500:
    print("you got 30per discount")
    
per = sum*10/100
print(per)    


