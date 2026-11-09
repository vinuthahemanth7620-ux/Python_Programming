# Write a program to check whether two strings are anagrams of each other.
String = str(input("Enter the String_1 :"))
String1 = str(input("Enter the String_2 :"))

String_1 =list(String)
String_2 = list(String1)

X = len(String_1)
Y = len(String_2)
if X == Y :
    print("The length of Two Strings are Equal")

String_1.sort()
String_2.sort()

if String_1 == String_2:
    print("The Two Strings are Anagrams")
else :
    print("The Two Strings are not Anagrams")





