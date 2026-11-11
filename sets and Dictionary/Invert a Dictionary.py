# Write a program to invert a dictionary (swap keys and values).

Dictionary = {
    "Apple" : 50,
    "Mango" : 60,
    "Banana" : 55,
    "Papaya" : 70,
    "Pineapple" :40
}

New_Dictionay = { }
for key in Dictionary:
    New_Dictionay[Dictionary[key]] = key 

print(" The Inverted Dictionary is :",New_Dictionay)

