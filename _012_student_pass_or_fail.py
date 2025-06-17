marks = []
print("Enter the marks of 5 subjects:")
for i in range(5):
    marks.append(int(input('')))

if (all(i >= 33 for i in marks) and sum(marks)/len(marks)>=40):
    print("Student passed")
else:
    print("Student failed")