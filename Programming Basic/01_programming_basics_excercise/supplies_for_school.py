pens = int(input())
markers = int(input())
liters = int(input())
discount = int(input())
total_pens = pens * 5.80
total_markers = markers * 7.20
total_liters = liters * 1.20
sum_without_discount = total_pens + total_markers + total_liters
total_sum = sum_without_discount - sum_without_discount * discount/100
print(total_sum)