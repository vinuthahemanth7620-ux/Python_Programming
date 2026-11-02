# Count the digits in an integer.
Number = int(input("Enter the number to Count :"))
Original_Number = Number

Number = abs(Number)

Count = 0
if Number == 0:
    Count = 1

else:   
    while Number > 0 : 
        Number = Number // 10
        Count += 1
print("The Total Count of a Given Number",Original_Number,"is",Count)