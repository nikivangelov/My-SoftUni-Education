n = int(input())
a = int(input())
b = int(input())
sum_pair = a + b
diff = 0
valid = True
for _ in range(2, n+1):
    current_a = int(input())
    current_b = int(input())
    current_sum = current_a + current_b

    if current_sum != sum_pair:
        valid = False
        diff = abs(current_sum - sum_pair)
        sum_pair = current_sum
if valid:
    print(f'Yes, value={sum_pair}')
else:
    print(f'No, maxdiff={diff}')