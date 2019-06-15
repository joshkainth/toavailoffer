number = int(input("Enter the value : "))
a = 0
b = 1
for i in range(0,number):
    c = a+b
    print("{} + {} = {}".format(a,b,c))
    a = b
    b = c