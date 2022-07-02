string = input()
vowels = ['a', 'o', 'u', 'e', 'i']
string_list = [ch for ch in string if ch not in vowels]
print("".join(string_list))
