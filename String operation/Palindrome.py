#Write a program to check whether a given string is a palindrome.

string = str(input("enter teh string: "))
print(string)
reversed = string[: : -1]

if string == reversed:
    print("the given string is Palindrome")
else:
    print("the given string is not a Palindrime")