#Write a program to remove leading and trailing spaces, 
#convert a sentence to lowercase, and display each word separately.

string = str(input("enter the string :"))
print(string)

new_string = string.strip( )
print("the string after removing the spaces:",new_string)

sentence = str(input("enter the sentence to perform operation :"))
L = sentence.lower()
U = sentence.upper()
print(" The sentence in the lowercase :", L)
print(" The sentence in the uppercase : ", U)

words = L.split()
print(" each word seperately in the sentence are :")
for i in words:
    print (i)