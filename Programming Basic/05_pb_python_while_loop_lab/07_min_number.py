import sys

n = input()
min = sys.maxsize

while n != 'Stop':
    num = int(n)
    if num <= min:
        min = num

    n = input()

print(min)