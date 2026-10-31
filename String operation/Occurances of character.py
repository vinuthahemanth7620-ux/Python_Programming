# Write a program to count the occurrences of a specified character in a string.

string = str(input("enter the string :"))
Character = str(input("enter the character to finding the occurances :"))

count=0
for i in string:
    if i == Character:
        count +=1
print(f" the number of {Character}'s in the given string {string} is: ", count)
