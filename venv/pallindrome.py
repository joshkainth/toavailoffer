lower = int(input("Enter the lower range"))
upper = int(input("Enter the upper range"))


for number in range(lower,upper+1):
    s = 0
    temp = number
    while number > 0:
        p = number % 10
        s = s * 10 + p
        number = number // 10

    if s == temp:
        print(temp,"Number Is palindrome")
    # else:
    #     print(temp,"Number is not palindrome")