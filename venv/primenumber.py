num = int(input("Enter The number : "))

if (num%2)==0:
    print(num,"is a prime number")
elif(num%3)==0:
    print(num, "is a prime number")
elif (num%5)==0:
    print(num, "is a prime number")
elif(num%7)==0:
    print(num, "is a prime number")
elif(num%11)==0:
    print(num, "is a prime number")
else:
    print(num, "is not prime number")