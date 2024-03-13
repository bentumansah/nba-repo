t_marks = 0
marks = input("Enter student marks: ").split()
for i in range(0, len(marks)):
    marks[i] = int(marks[i])
    t_marks += marks[i]
avg =  t_marks / len(marks)
print(avg)