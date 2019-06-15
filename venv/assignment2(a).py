first_number = int(input("Enter the First Number : "))
second_number = int(input("Enter the Second Number : "))

def max():
    if first_number>second_number:
        print("This Number {} is Greater ".format(first_number))
    else:
        print("This Number {} is Greater ".format(second_number))


if first_number<second_number:
        print("This Number {} is Smaller ".format(first_number))
else:
        print("This Number {} is Smaller ".format(second_number))

add= first_number+second_number
print("Sum of Two Number : ", add)

# a = max()
# c = sum()
# b = min()

print(max())
print(min())
print(sum())