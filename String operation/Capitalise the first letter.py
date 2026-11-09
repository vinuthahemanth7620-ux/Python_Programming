# Write a program to capitalize the first letter of every word without using title().
Sentence = str(input("Enter the Sentence :"))

Split_String = Sentence.split()
Result = " "
for i in Split_String:
    Result += i.capitalize()
print("The Capitalized string is :",Result)


   

