m1 = int(input("Enter marks1: "))
m2 = int(input("Enter marks2: "))
m3 = int(input("Enter marks3: "))

total = m1 + m2 + m3
per = (total / 300) * 100   # correct percentage formula

print("Percentage =", per)

if per >= 40:
    print("Pass")
else:
    print("Fail")
