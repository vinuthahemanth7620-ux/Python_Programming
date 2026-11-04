# Use map() and a lambda function to double every number in a list.

Number = [10,20,30,40,50]
Double_Number = map(lambda Number : Number * 2, Number)
Result = list(Double_Number)
print("The double of every number in a list is :", Result )