def gettinginput():
    billamount = int(input("Enter the Amount : "))
def calculatetaxesonbill(gettinginput): #Function with arguement in Python
    tax = gettinginput * (18 / 100)
    print("For {} amount taxes are {}".format(billamount, tax))

print("Calculatetaxesonbill : ",calculatetaxesonbill)

def calculatetaxesonbill(gettinginput): #Function with arguement and return in Python
    tax = gettinginput * (18 / 100)
    return tax

print("Calculatetaxesonbill : ",calculatetaxesonbill)

print("Tax : {}".format(calculatetaxesonbill))
# calculatetaxesonbill(100)
# calculatetaxesonbill(300)