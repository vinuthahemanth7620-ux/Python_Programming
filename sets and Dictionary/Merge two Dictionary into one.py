# Write a program to merge two dictionaries into one dictionary.

dictionary = {
    "name" : "Vinutha",
    "age" :  26
}

dictionary_2 = {
   "Course" : ['ml','dl'],
    "Marks" : 95
}

dictionary.update(dictionary_2)
print("The Mergerd Dictionary :",dictionary)