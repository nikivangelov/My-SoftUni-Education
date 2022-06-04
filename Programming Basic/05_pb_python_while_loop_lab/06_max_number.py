import sys

n = input()
max = - sys.maxsize

while n != 'Stop':
    num = int(n)
    if num >= max:
        max = num

    n = input()

print(max)