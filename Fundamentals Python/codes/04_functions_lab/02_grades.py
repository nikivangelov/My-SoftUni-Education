def grades(each_grade):
    result = ''
    if 2.00 <= each_grade <= 2.99:
        result = 'Fail'
    elif 3.00 <= each_grade <= 3.49:
        result = 'Poor'
    elif 3.50 <= each_grade <= 4.49:
        result = 'Good'
    elif 4.50 <= each_grade <= 5.49:
        result = 'Very Good'
    elif 5.50 <= each_grade <= 6.00:
        result = 'Excellent'
    return result


current_grade = float(input())
print(grades(current_grade))