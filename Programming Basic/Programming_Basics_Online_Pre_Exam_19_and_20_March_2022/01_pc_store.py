proccessor_price_usd = float(input())
video_card_price_usd = float(input())
ram_price_usd = float(input())
ram_number = int(input())
discount = float(input())

proccessor_price_bgn = proccessor_price_usd * 1.57
video_card_price_bgn = video_card_price_usd * 1.57
ram_price_bgn = ram_price_usd * 1.57
total_ram_price = ram_price_bgn * ram_number
total_proccessor_price = proccessor_price_bgn - proccessor_price_bgn * discount
total_video_card_price = video_card_price_bgn - video_card_price_bgn * discount

total_price = total_proccessor_price + total_video_card_price + total_ram_price
print(f'Money needed - {total_price:.2f} leva.')


