amount = int(input("Enter the Amount : "))
print("1. Zomato  2. Swiggy001")
promocode = input("\nEnter the Promocode :")
if promocode == "Zomato":
        print("We have given offer of 20%")
        discount_price = 0.2*amount
        print("Discount Price : ", discount_price)
        actual_price = amount - discount_price
        print("Payable Amount : ", actual_price)
elif promocode == "Swiggy001":
        print("We have given offer of 40%")
        discount_price = 0.4*amount
        print("Discount Price : ",discount_price)
        actual_price = amount-discount_price
        print("Payable Amount : ",actual_price)
else:
    print("Discount Price : 0")
    #actual_price = amount - discount_price
    print("Payable Amount : ", amount)