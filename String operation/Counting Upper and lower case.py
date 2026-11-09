# Write a program to count uppercase letters, 
# lowercase letters, digits and special characters in a string.

String = str(input("Enter the String :"))

Upper_case = 0
Lower_case = 0
Digits = 0
Special_Characters = 0

for i in String:
    if i.isupper():
        Upper_case += 1
    elif i.islower():
        Lower_case +=1
    elif i.isdigit():
        Digits +=1
    elif not i.isspace():
        Special_Characters +=1

print("The number of Lowercase :",Lower_case)
print("The number of Uppercase :",Upper_case)
print("The number of Digits :",Digits)
print("The number of Special_Characters :",Special_Characters)


