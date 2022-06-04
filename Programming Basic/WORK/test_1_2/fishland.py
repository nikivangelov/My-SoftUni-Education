boredom_price = float(input())
sprat_price = float(input())
bonito = float(input())
scad = float(input())
mussels = int(input())
bonito_price = boredom_price + boredom_price * 0.6
scad_price = sprat_price + sprat_price * 0.8
total_price = bonito * bonito_price + scad * scad_price + mussels * 7.5
print(f'{total_price:.2f}')
