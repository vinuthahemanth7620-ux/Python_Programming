# Write a program to remove duplicate words from a sentence using sets.
Sentence = input("Enter the Sentence :")
L = Sentence.split()

Seen = set()
New_list = []
for i in L:
    if i not in Seen:
        New_list.append(i)
        Seen.add(i)

Result = " ".join(New_list)
print("The New sentence after removing Duplicate :", Result)