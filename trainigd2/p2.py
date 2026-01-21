n = int(input("Enter a non-negative number: "))
steps = 0

while n > 0:
    if n % 2 == 0:   
        n = n // 2
    else:             
        n = n - 1
    steps = steps + 1

print(f"Number of steps to reduce to zero: {steps}")
