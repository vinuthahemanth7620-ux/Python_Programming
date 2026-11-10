# Write a program to check whether a string contains only digits without using isdigit()
String = str(input("Enter the String :"))

for i in String:
    if i < '0' or i > '9':
        print("The String doesnot contain only Digits")
        break
else:
    print("The String contains only Digits")




