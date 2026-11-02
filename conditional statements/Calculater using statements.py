# Write a simple calculator using if-elif-else for addition, subtraction, multiplication, and division.
Number_1 = int(input("Enter the Number 1 :"))
Number_2 = int(input("Enter the Number 2 :"))

Operation = input("Choose the Operation to perform(A/S/M/D) :")
if Operation == "A":
    print("The Sum of Two numbers is :", Number_1 + Number_2)

elif Operation == "S":
    print("The difference between Two numbers is :", Number_1 - Number_2)

elif Operation == "M":
    print("The Product of Two Numbers are :", Number_1 * Number_2)

elif Operation == "D":
    if Number_2 == 0:
        print("Division is Not Possible.")
    else:
        print("The Division of Two numbers are :",Number_1/Number_2)

else:
    print("You entered an invalid operator")