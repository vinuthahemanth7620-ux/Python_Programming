# Write a program to determine whether a number
# is positive, negative or zero using comparison and logical operators.

number = int(input("enter the value = "))
print(number)

if number > 0:
    print("positive number", number)
elif number < 0:
    print("negative number", number)
else:
    print("the number is Zero")