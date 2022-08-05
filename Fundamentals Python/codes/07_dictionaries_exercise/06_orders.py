products = {}
current_product = input().split(' ')
while current_product[0] != 'buy':
    product_name = current_product[0]
    price = float(current_product[1])
    quantity = int(current_product[2])
    if product_name not in products:
        products[product_name] = {}
        products[product_name]['price'] = 0
        products[product_name]['quantity'] = 0
    products[product_name]['price'] = price
    products[product_name]['quantity'] += quantity
    current_product = input().split(' ')

for key, value in products.items():
    current_value = products[key]['price'] * products[key]['quantity']
    print(f"{key} -> {current_value:.2f}")
