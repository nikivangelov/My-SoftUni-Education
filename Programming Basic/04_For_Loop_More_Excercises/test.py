period = int(input())

treated = 0
untreated = 0
doctors = 7

for day in range(1, period + 1):
    patients = int(input())

    if patients > doctors and day % 3 != 0:
        treated += doctors
        untreated += patients - doctors
    elif patients <= doctors and day % 3 != 0:
        treated += patients

    if day % 3 == 0 and untreated > treated:
        if patients > doctors:
            doctors += 1
            treated += doctors
            untreated += patients - doctors
        else:
            doctors += 1
            treated += patients
    elif day % 3 == 0 and treated >= untreated:
        if patients > doctors:
            treated += doctors
            untreated += patients - doctors
        else:
            treated += patients
print(f"Treated patients: {treated}.")
print(f"Untreated patients: {untreated}.")