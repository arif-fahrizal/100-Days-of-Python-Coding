# new_dict = { new_key: new_value for (key, value) in dict.items() if test}
import random
import pandas

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
students_scores = { student: random.randint(1,100) for student in names}
passed_students = { student: score for (student, score) in students_scores.items() if score >= 60}

# Pandas Iterrows
student_dict = {
    "students": ["Alex", "Beth", "Caroline"],
    "score": [72, 60, 88]
}
student_df = pandas.DataFrame(student_dict)
print(student_df)
for (index, row) in student_df.iterrows():
    print(row.students)

print(students_scores)
print(passed_students)