obtained = False
materials_dict = {'shards': 0, 'fragments': 0, 'motes': 0}
while True:
    materials_stats = input().split(" ")
    for i in range(1, len(materials_stats), 2):
        quantity = int(materials_stats[i - 1])
        material = materials_stats[i].lower()
        if material not in materials_dict.keys():
            materials_dict[material] = 0
        materials_dict[material] += quantity
        if materials_dict['shards'] >= 250:
            materials_dict['shards'] -= 250
            print("Shadowmourne obtained!")
            obtained = True
            break
        elif materials_dict['fragments'] >= 250:
            materials_dict['fragments'] -= 250
            print("Valanyr obtained!")
            obtained = True
            break
        elif materials_dict['motes'] >= 250:
            materials_dict['motes'] -= 250
            print("Dragonwrath obtained!")
            obtained = True
            break
    if obtained:
        break

for key, value in materials_dict.items():
    print(f'{key}: {value}')