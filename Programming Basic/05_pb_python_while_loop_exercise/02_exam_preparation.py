unsatisfied_grades = int(input())
unsatisfied_counter = 0
grades_counter = 0
grades_sum = 0
last_task = ''
while unsatisfied_counter < unsatisfied_grades:
    task_name = input()
    if task_name != 'Enough':
        last_task = task_name
        task_grade = int(input())
        grades_counter += 1
        grades_sum += task_grade
        if task_grade <= 4:
            unsatisfied_counter += 1
            if unsatisfied_counter == unsatisfied_grades:
                print(f'You need a break, {unsatisfied_counter} poor grades.')
                break
    else:
        print(f'Average score: {grades_sum / grades_counter :.2f}')
        print(f'Number of problems: {grades_counter}')
        print(f'Last problem: {last_task}')
        break


