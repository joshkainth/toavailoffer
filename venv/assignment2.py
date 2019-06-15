first_number = int(input("Enter the First Number : "))
second_number = int(input("Enter the Second Number : "))

def max():
    if first_number>second_number:
        print("This Number ",first_number, " is Greater ")
    else:
        print("This Number ",second_number, " is Greater ")

def min():
    if first_number<second_number:
        print("This Number ",first_number, " is Smaller ")
    else:
        print("This Number ",second_number, " is Smaller ")

def sum():
    add= first_number+second_number
    print("Sum of Two Number : ", add)   #print("Sum of Two Number : ", add)

max()
min()
sum()