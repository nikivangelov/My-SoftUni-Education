from math import floor

planned_processor_number = int(input())
employees_number = int(input())
working_days = int(input())

total_working_time = employees_number * working_days * 8
processors = floor(total_working_time / 3)
diff = abs((planned_processor_number - processors) * 110.1)
if planned_processor_number <= processors:
    print(f'Profit: -> {diff:.2f} BGN')
else:
    print(f'Losses: -> {diff:.2f} BGN')