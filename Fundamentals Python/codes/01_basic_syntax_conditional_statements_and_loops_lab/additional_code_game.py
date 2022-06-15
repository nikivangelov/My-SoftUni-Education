import random

guess_counter = 0
answered_questions = []
questions = ['Кога е основана България?', 'Колко е 2*2?', 'Кой спечели купата на България през 2022?']
for _ in range(10):
    current_question = random.choice(questions)
    if current_question not in answered_questions:
        answered_questions.append(current_question)
        print(current_question)
    else:
        continue

    if current_question == 'Кога е основана България?':
        answer = input('Моля въведете вашия отговор: ')

        if answer == '681':
            print('Верен отговор!\n')
            guess_counter += 1
        else:
            print(f'Грешен отговор \n')

    elif current_question == 'Колко е 2*2?':
        answer = input('Моля въведете вашия отговор: ')

        if answer == '4':
            print('Верен отговор!\n')
            guess_counter += 1
        else:
            print(f'Грешен отговор \n')

    elif current_question == 'Кой спечели купата на България през 2022?':
        answer = input('Моля въведете вашия отговор: ')

        if answer == 'Левски':
            print('Верен отговор!\n')
            guess_counter += 1
        else:
            print(f'Грешен отговор \n')

    if guess_counter == 2:
        print(f'Ти спечели играта!')
        break