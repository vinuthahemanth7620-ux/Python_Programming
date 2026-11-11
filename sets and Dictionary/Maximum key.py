# Write a program to find the key associated with the maximum value in a dictionary.
Dictionary = {
    "Apple" : 50,
    "Mango" : 60,
    "Banana" : 55,
    "Papaya" : 70
}

Max_Key = max(Dictionary, key = Dictionary.get)
print("The Maximum Key is :",Max_Key)
print("The Maximum value is :",Dictionary[Max_Key])