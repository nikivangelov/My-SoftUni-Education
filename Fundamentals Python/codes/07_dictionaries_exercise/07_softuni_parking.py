number = int(input())
registered_drivers = {}
for i in range(number):
    command = input().split(' ')
    driver_name = command[1]
    if command[0] == 'register':
        plate_number = command[2]
        if driver_name not in registered_drivers:
            print(f"{driver_name} registered {plate_number} successfully")
            registered_drivers[driver_name] = plate_number
        else:
            print(f"ERROR: already registered with plate number {plate_number}")
    elif command[0] == 'unregister':
        if driver_name not in registered_drivers:
            print(f"ERROR: user {driver_name} not found")
        else:
            print(f"{driver_name} unregistered successfully")
            del registered_drivers[driver_name]

for key, value in registered_drivers.items():
    print(f"{key} => {value}")