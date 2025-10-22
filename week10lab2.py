student_grades = {
    "Alice": 85, 
    "Bob": 92,
    "Charlie": 80,
    "Diana": 95
}

def caluclate_average_grade(student_grades):
    total = 0
    for grades in student_grades:
        total += student_grades[grades]
    average = total / len(student_grades)
    print(average)
caluclate_average_grade(student_grades)

