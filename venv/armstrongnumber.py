number = int(input("Enter the Number : "))
order = len(str(number))
s = 0
temp = number
while temp>0:
    p = temp%10
    s += p**order
    temp//=10

if number==s:
    print("Number Is armstrong")
else:
    print("Number is not armstrong")