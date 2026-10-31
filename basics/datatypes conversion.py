#Write a program to accept a number and convert it into a float and a string. Display the resulting types.
number = int(input("enter the number:"))
print(number)

X = float(number)
print("The value of X is:" , X)
print("the type of X is:" ,type(X))

Y = str(number)
print("The value of Y is:", Y)
print("the type of Y is:", type(Y))


