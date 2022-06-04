n = int(input())
salary = float(input())
condition = False
for i in range(n):
    tab = input()
    if tab == 'Facebook':
        salary -= 150
    elif tab == 'Instagram':
        salary -= 100
    elif tab == 'Reddit':
        salary -= 50
    if salary <= 0:
        condition = True
        break
if not condition:
    print(int(salary))
else:
    print('You have lost your salary.')



