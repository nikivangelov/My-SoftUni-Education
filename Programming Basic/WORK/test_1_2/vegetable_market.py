N = float(input())
M = float(input())
vegetables_kg = int(input())
fruits_kg = int(input())
total_vegetables = N * vegetables_kg / 1.94
total_fruits_euros = M * fruits_kg / 1.94
total_price = total_vegetables + total_fruits_euros
print(f'{total_price:.2f}')
