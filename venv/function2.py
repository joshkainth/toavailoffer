#pass by reference

def squareofnumbers(numbers):
    print("Number is : ",numbers,hex(id(numbers)))
    for i in range(0,len(numbers)):
        #print(numbers[i])
        numbers[i] = numbers[i] * numbers[i]

n = [1,2,3,4,5] #using reference of list
print("n : ",n,hex(id(n)))
squareofnumbers(n)
print(n)