period = int(input())
number_of_doctors = 7
treated_patients = 0
untreated_patients = 0
for i in range(1, period + 1):
    number_of_patients = int(input())

    if i % 3 == 0 and treated_patients < untreated_patients:
        number_of_doctors += 1

    if number_of_patients <= number_of_doctors:
        treated_patients += number_of_patients

    else:
        treated_patients += number_of_doctors
        untreated_patients += (number_of_patients - number_of_doctors)


print(f'Treated patients: {treated_patients}.')
print(f'Untreated patients: {untreated_patients}.')


