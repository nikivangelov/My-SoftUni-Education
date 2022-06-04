V = int(input())
P1 = int(input())
P2 = int(input())
H = float(input())
liters_P1 = P1 * H
liters_P2 = P2 * H
total_liters = liters_P1 + liters_P2
if total_liters <= V:
    percent_full = total_liters / V * 100
    percent_P1 = liters_P1 / total_liters * 100
    percent_P2 = liters_P2 / total_liters * 100
    print(f"The pool is {percent_full:.2f}% full. Pipe 1: {percent_P1:.2f}%. Pipe 2: {percent_P2:.2f}%.")
else:
    diff = total_liters - V
    print(f"For {H} hours the pool overflows with {diff} liters.")
