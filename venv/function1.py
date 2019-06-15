#pass by value
def squareofnumber(num):
    print("Hashcode of num ",hex(id(num)))
    num = num*num
    print("Num is : ",num)
    print("Hashcode of num now is ", hex(id(num)))
    return num

n= 10
print("Hashcode of n ",hex(id(n)))
squareofnumber(n)
print("n is : ",n)