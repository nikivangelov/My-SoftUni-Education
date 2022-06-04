actor_name = input()
academy_points = float(input())
n = int(input())
total_points = academy_points
condition = False

for i in range(n):
    name_of_jury = input()
    jury_points = float(input())
    total_points += (len(name_of_jury) * jury_points) / 2
    if total_points >= 1250.5:
        condition = True
        break

if not condition:
    print(f'Sorry, {actor_name} you need {(1250.5 - total_points):.1f} more!')
else:
    print(f'Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!')