number = int(input("Enter the Number : "))
s = 0
if number>0:
    p = number%10
    s = s+p
    number = int( number /10)
print(s)