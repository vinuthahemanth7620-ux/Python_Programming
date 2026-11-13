# Write a program to find the shortest word in a sentence.
Sentence = str(input("Enter the Sentence :"))

L = Sentence.split( )
for i in L:
    print(i)

Shortest_Word = L[0]
for words in L :
    if len(words) < len(Shortest_Word):
        Shortest_Word = words

print("The Shortest word in the sentence is :",Shortest_Word)
