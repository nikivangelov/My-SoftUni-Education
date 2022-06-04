num_of_loads = int(input())
type_of_transportation = ''
price = 0
bus_load = 0
truck_load = 0
train_load = 0
for load in range(num_of_loads):
    weight = int(input())
    if weight <= 3:
        type_of_transportation = 'bus'
        price += weight * 200
        bus_load +=weight
    elif 4 <= weight <= 11:
        type_of_transportation = 'truck'
        price += weight * 175
        truck_load += weight
    else:
        type_of_transportation = 'train'
        price += weight * 120
        train_load += weight

print(f'{price / (bus_load + truck_load + train_load):.2f}')
print(f'{bus_load / (bus_load + truck_load + train_load) * 100:.2f}%')
print(f'{truck_load / (bus_load + truck_load + train_load) * 100:.2f}%')
print(f'{train_load / (bus_load + truck_load + train_load) * 100:.2f}%')