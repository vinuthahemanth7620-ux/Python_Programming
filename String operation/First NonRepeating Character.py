# Write a program to find the first non-repeating character in a string.
String = str(input("Enter the string :"))

for i in String:
    if String.count(i) == 1 :
        print("The first non-Repeating Character is",i)
        break
else:
    print("The non-repeating Character is not found.")