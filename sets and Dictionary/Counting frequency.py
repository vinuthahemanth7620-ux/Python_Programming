# Write a program to count the frequency of each character in a string using a dictionary.

String = str(input("Enter the String :"))
Frequency = { }

for i in String:
    if i in Frequency:
        Frequency[i] +=1
    else:
        Frequency[i] = 1
print(" The Frequency of each character in the given string :", Frequency)
