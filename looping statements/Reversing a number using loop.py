# Reverse a number using a loop.
Number = int(input("Enter the Number to Reverse :"))
Original_Number = Number

Reverse = 0
while Number > 0:
    Digit = Number % 10
    Reverse = Reverse * 10 + Digit
    Number = Number // 10 
print("The Reverse of a Given Number",Original_Number,"is :",Reverse)
