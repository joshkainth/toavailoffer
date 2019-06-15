def calculatetaxesonbill(): #Function in Python
    billamount = int(input("Enter the amount : "))
    tax = billamount * (18 / 100)
    print("For {} amount taxes are {}".format(billamount, tax))

n = int(input("How many bills you wish to process : "))
for i in range(1,n+1):
    calculatetaxesonbill() # Function Calling

print("Thank You !!")