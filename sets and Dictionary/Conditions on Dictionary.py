# Write a program to create a dictionary containing student names and marks,
# then display students who scored above 75.

Students = {
    "Vinutha": 85,
    "Rahul": 70,
    "Anu": 90,
    "Kiran": 65,
    "Priya": 80
}

for i in Students:
    if Students[i] > 75:
        print(i,":",Students[i])