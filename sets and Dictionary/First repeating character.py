#Find the first repeating character in a string.
String = str(input("Enter the string :"))

New_string = " "
for i in String:
    if i not in New_string:
        New_string += i 
    else:
        print(" the First Repeating Character in a string is :", i)
        break
print(" the Characters in the New String are :", New_string)