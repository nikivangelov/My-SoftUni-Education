def even_odd_sum(num):
    even_sum = 0
    odd_sum = 0
    for _ in range(len(str(num))):
        current_num = num % 10
        if current_num % 2 == 0:
            even_sum += current_num
        else:
            odd_sum += current_num
        num = num // 10
    result = f"Odd sum = {odd_sum}, Even sum = {even_sum}"
    return result


number = int(input())
print(even_odd_sum(number))