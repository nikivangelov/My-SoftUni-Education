deposit = float(input())
months = int(input())
anual_rate = float(input())
monthly_rate = (anual_rate / 12) / 100
monthly_sum = deposit * monthly_rate
total_sum = deposit + months * monthly_sum
print(total_sum)