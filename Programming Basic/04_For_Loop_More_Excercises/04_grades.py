num_of_students = int(input())
sum_of_grades = 0
failed_students = 0
average_students = 0
very_good_students = 0
top_students = 0
for _ in range(1, num_of_students + 1):
    grade = float(input())
    sum_of_grades += grade
    if 2 <= grade <= 2.99:
        failed_students += 1
    elif 3 <= grade <= 3.99:
        average_students += 1
    elif 4 <= grade <= 4.99:
        very_good_students += 1
    elif 5 <= grade <= 6:
        top_students += 1

p1 = top_students / num_of_students * 100
p2 = very_good_students / num_of_students * 100
p3 = average_students / num_of_students * 100
p4 = failed_students / num_of_students * 100
print(f"Top students: {p1:.2f}%")
print(f"Between 4.00 and 4.99: {p2:.2f}%")
print(f"Between 3.00 and 3.99: {p3:.2f}%")
print(f"Fail: {p4:.2f}%")

print(f'Average: {sum_of_grades / num_of_students :.2f}')