# Write a program to reverse each word in a sentence while maintaining the original word order.

Sentence = str(input("Enter the Sentence :"))
L = Sentence.split()

New_String = " "
for i in L:
    New_String =New_String + i[: :-1] + " "
print("The reversed String :",New_String)
    