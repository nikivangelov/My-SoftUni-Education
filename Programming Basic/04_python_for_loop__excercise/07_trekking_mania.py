num_of_groups = int(input())
climbers_for_moussala = 0
climbers_for_monblan = 0
climbers_for_kilimandjaro = 0
climbers_for_k2 = 0
climber_for_everest = 0
total_climbers = 0
for i in range(num_of_groups):
    climbers_in_group = int(input())
    total_climbers += climbers_in_group
    if climbers_in_group <= 5:
        climbers_for_moussala += climbers_in_group
    elif 6 <= climbers_in_group <= 12:
        climbers_for_monblan += climbers_in_group
    elif 13 <= climbers_in_group <= 25:
        climbers_for_kilimandjaro += climbers_in_group
    elif 26 <= climbers_in_group <= 40:
        climbers_for_k2 += climbers_in_group
    else:
        climber_for_everest += climbers_in_group

print(f'{(climbers_for_moussala / total_climbers * 100):.2f}%')
print(f'{(climbers_for_monblan / total_climbers * 100):.2f}%')
print(f'{(climbers_for_kilimandjaro / total_climbers * 100):.2f}%')
print(f'{(climbers_for_k2 / total_climbers * 100):.2f}%')
print(f'{(climber_for_everest / total_climbers * 100):.2f}%')