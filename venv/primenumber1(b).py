starting_number = int(input("Enter Starting number : "))
ending_number = int(input("Enter Ending number : "))

for num in range(starting_number,ending_number+1):
    if num >1:
        for i in range(2, num):
            if (num % i) == 0:
                #print(num, "is not a prime number")
                break
        else:
            print(num, "is prime number")