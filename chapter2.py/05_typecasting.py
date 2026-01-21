a = 77

t = type(a)   # class <int>
print(t)


a = 72.05

t = type(a)   # class <float>
print(t)


a = "anishop"

t = type(a)   # class <str>
print(t)


a = True 

t = type(a)   # class <bool>
print(t)



a = None

t = type(a)   # class <Nonetype>
print(t)


a = "77"
b = float(a)   # string is converted into float
t = type(b)   
print(t)


a = 77.5
b = str(a)   # float is converted into str
t = type(b)   
print(t)


a = "7855"
b = int(a)   # string is converted into int
t = type(b)   
print(t)


a = 7855
b = float(a)   # integer is converted into float
t = type(b)   
print(t)