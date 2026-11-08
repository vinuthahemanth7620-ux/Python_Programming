#Write a program to count the number of vowels in a string.

string = str(input("enter the string :"))
vowels = ['a', 'e','i','o','u']
count = 0
for i in string:
    if i in vowels:
        count +=1

print("The Given String is :",string)       
print("The number of vowels in string:", count)


