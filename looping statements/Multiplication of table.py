# Print the multiplication table of a number entered by the user.
Number = int(input("Enter the number to print table :"))

for i in range(1,11):
    print(Number,"x",i,"=",Number * i)
print(" The Multiplication Table of given number",Number,"done")
    