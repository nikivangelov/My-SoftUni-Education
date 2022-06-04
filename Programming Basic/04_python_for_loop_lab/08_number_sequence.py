import sys

n = int(input())
min_num = sys.maxsize
max_num = -sys.maxsize
for i in range(1, n+1):
    a = int(input())
    if a > max_num:
        max_num = a
    if a < min_num:
        min_num = a

print(f'Max number: {max_num}')
print(f'Min number: {min_num}')