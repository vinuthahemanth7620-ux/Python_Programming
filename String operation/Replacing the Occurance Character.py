# Write a program to replace all occurrences of a particular character with another character.
String = str(input("Enter the String :"))
Character = str(input("Enter the Selected Character :"))
Character1 = str(input("Enter the Replacing Character : "))

New_String = " "
Count = 0

for i in String:
    if i == Character:
        Count +=1
        New_String = New_String + Character1
    else :
        New_String = New_String + i

print("The Number of Occurance Character is : ",Count)
print("The String Before Replacing with", Character1,"is :",String)
print("The String After Replacing with", Character1,"is :",New_String)
