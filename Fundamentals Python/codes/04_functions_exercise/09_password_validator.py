def pass_is_valid(string):
    digit_count = 0
    result = ''
    is_valid = True
    for i in range(len(string)):
        if ord(string[i]) in range(65, 90) or ord(string[i]) in range(97, 122):
            continue
        elif ord(string[i]) in range(48, 57):
            digit_count += 1
        else:
            print("Password must consist only of letters and digits")
            is_valid = False
            break
    if len(string) < 6 or len(string) > 10:
        print(f"Password must be between 6 and 10 characters")
        is_valid = False
    if digit_count < 2:
        result = f"Password must have at least 2 digits"
        is_valid = False
    if is_valid:
        result = f"Password is valid"
    return result


password = input()
print(pass_is_valid(password))