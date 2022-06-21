def repeat_string(text, num: int):
    result = num * text
    return result


string = input()
count = int(input())
print(repeat_string(string, count))