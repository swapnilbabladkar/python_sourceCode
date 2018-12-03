# Grading of students
# >90 Outstanding, >80 Excellent, >=60 Very Good, <60 Others

num = input('Enter marks:')
grade=''
if (num > 90):
    grade='Outstanding'
elif (num > 80):
    grade = "Excellent"
elif (num >= 60):
    grade = "Very Good"
else:
    grade = "Others"

print "Number= ", num, " Grade: ", grade
