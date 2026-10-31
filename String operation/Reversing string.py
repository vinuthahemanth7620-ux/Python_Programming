# Write a program to reverse a string without using a built-in reverse function.

#approach-1
string = str(input("enter the string :"))
reverse = " "
for i in string:
    reverse = i + reverse

print("original string is :" ,string)
print("the reversed string is:" ,reverse)

#approach-2
string = str(input("enter the string :"))
A = string[: :-1]
print(A)
print("original string is :" ,string)
print("the reversed string is :" ,A)
