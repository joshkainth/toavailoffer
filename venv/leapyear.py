starting_year = int(input("Enter Starting Year : "))
ending_year = int(input("Enter Ending Year : "))

for year in range(starting_year,ending_year+1):
    if (year%4)==0:
        print(year,"is a leap year")
    else :
        print(year, "is not a leap year")