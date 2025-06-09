# Program to store and display sorted marks of students
marks = []
no_of_students = int(input("Enter the number of students whose marks you want to enter:\n"))
for i in range(no_of_students):
    entered_marks = int(input(f"Enter the marks of student number {i+1}:\n"))
    marks.append(entered_marks)
    marks.sort()
print("The sorted marks of the students are:\n" + str(marks))