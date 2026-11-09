# Write a program to check whether a number is divisible by both 5 and 11.
Number_1 = int(input("Enter the number :"))

if Number_1 % 5 ==0 and Number_1 % 11 == 0:
    print("The given number is divided by 11 and 5")
else:
    print("The given number is not divided by 11 and 5")

