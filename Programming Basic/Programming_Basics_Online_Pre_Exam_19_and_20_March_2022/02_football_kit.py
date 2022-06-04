t_shirt_price = float(input())
total_price_goal = float(input())
shorts_price = 0.75 * t_shirt_price
socks_price = 0.2 * shorts_price
shoes_price = (t_shirt_price + shorts_price) * 2
total_price = 0.85 * (t_shirt_price + shorts_price + socks_price + shoes_price)
if total_price >= total_price_goal:
    print(f'Yes, he will earn the world-cup replica ball!')
    print(f'His sum is {total_price:.2f} lv.')
else:
    print(f'No, he will not earn the world-cup replica ball.')
    print(f'He needs {(total_price_goal - total_price):.2f} lv. more.')