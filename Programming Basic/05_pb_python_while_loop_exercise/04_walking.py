total_steps = 0
while total_steps < 10000:
    step = input()
    if step == 'Going home':
        additional_steps = int(input())
        total_steps += additional_steps
        break

    total_steps += int(step)

diff = abs(total_steps - 10000)
if total_steps >= 10000:
    print('Goal reached! Good job!')
    print(f'{diff} steps over the goal!')
else:
    print(f'{diff} more steps to reach goal.')