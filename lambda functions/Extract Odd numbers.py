# Use filter() to extract all odd numbers from a list.

Numbers = [1,2,3,4,5]
Odd_Numbers = filter(lambda Numbers : Numbers % 2 != 0, Numbers)
Result = list(Odd_Numbers)
print("The odd Numbers in the given list :",Result)
