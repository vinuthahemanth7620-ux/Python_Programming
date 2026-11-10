# Write a program to find the common keys between two dictionaries.
dictionary_1 = {
    "name" : "vinu",
    "age" : 12,
    "marks" :100
}

dictionary_2 = {
    "name" : "Ranju",
    "age" : 20,
    "Course" :['dl','ml']
}

New_key = [ ]
for i in dictionary_1:
    if i in dictionary_2:
        New_key.append(i)
print("The Common keys in two Dictionary are :",New_key) 