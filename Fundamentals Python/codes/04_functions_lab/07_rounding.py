# print(list(map(lambda x: round(float(x)), input().split(' '))))

def round_float(a):
    result = [round(num) for num in a]
    return result


float_list = list(map(float, input().split(' ')))
print(round_float(float_list))

