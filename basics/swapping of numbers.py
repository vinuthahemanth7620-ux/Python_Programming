# Write a program to swap two variables. (with a third variable)
a = 5
b = 10
print("Before swapping:" "a=",a , "b=",b)
c = a
a = b
b = c
print("After Swapping:" "a=",a   , "b=",b)


# Write a program to swap two variables. (without a third variable)
a = int(input("enter the value of a = "))
b = int(input("enter the value of b = "))
print("Before swapping:" "a=", a  , "b=", b)
a, b = b, a
print("After Swapping:" "a=",a , "b=",b)
