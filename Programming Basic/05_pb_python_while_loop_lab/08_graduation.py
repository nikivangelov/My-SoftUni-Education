student = input()
grades = 1
sum_grades = 0
excluded = 0
bad_grade_condition = False
while grades <= 12:
    grade = float(input())
    if grade < 4:
        excluded += 1

        if excluded > 1:
            print(f'{student} has been excluded at {grades} grade')
            bad_grade_condition = True
            break

        continue
    grades += 1
    sum_grades += grade
if not bad_grade_condition:
    print(f"{student} graduated. Average grade: {sum_grades / 12:.2f}")