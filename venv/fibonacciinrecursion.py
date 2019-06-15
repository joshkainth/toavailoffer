number = int(input("Enter the value : "))
#for i in range(0,number):
fibo = 0
print(fibo(number))

def fibo(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)