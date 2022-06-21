def abs_value(input_value):
    result = [abs(value) for value in input_value]
    return result


numbers = list(map(float, input().split(' ')))
print(abs_value(numbers))