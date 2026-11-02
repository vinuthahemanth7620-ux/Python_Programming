# Write a program to calculate a student's grade based on marks.
Marks = int(input("Enter the Marks to calculate Grade :"))

if Marks > 90:
    print("Student got A+ Grade.")
elif Marks > 80:
    print("Student got A Grade.")
elif Marks > 70:
    print("Student got B+ Grade.")
elif Marks > 60:
    print("Student got C Grade.")
else:
    print("Student is Failed in Exam")