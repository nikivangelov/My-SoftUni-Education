period = int(input())
electricity_bill = 0
water_bill = 0
internet_bill = 0
other_bills = 0
for _ in range(1, period + 1):
    electricity = float(input())
    electricity_bill += electricity
    water_bill += 20
    internet_bill += 15
    other_bills += (electricity + 20 + 15) * 1.2

print(f'Electricity: {electricity_bill:.2f} lv')
print(f'Water: {water_bill:.2f} lv')
print(f'Internet: {internet_bill:.2f} lv')
print(f'Other: {other_bills:.2f} lv')
print(f'Average: {(electricity_bill + water_bill + internet_bill + other_bills) / period :.2f} lv')