# Write a program to sort a dictionary based on its values.
Dictionary = {
    "Apple" : 50,
    "Mango" : 60,
    "Banana" : 55,
    "Papaya" : 70,
    "Pineapple" :40
}

New_Dict = { }
for key in sorted(Dictionary,key =Dictionary.get):
    New_Dict[key] = Dictionary[key]

print("The Sorted Dictionary :",New_Dict)
    
