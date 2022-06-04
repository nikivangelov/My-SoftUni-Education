import sys

n = int(input())

max_num = -sys.maxsize
sum = 0
for i in range(n):
    num = int(input())
    sum += num
    if num >= max_num:
        max_num = num

sum = sum - max_num
if max_num == sum:
    print('Yes')
    print(f'Sum = {sum}')
else:
    diff = abs(sum - max_num)
    print('No')
    print(f'Diff = {diff}')