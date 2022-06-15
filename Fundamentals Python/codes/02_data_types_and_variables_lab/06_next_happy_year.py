import sys
happy_year_status = False
first_year = input()
happy_year = ''

for next_year in range(int(first_year) + 1, sys.maxsize):
    happy_year = ''
    next_year = str(next_year)
    lenght = len(next_year)
    for digit in range(lenght):
        current_digit = next_year[digit]
        if current_digit not in happy_year:
            happy_year += current_digit
            if digit + 1 == lenght:
                happy_year_status = True
        else:
            break
    if happy_year_status:
        print(happy_year)
        break






    #if next_year[0] != next_year[1] and next_year[0] != next_year[2] and next_year[0] != next_year[3]:
        #if next_year[1] != next_year[2] and next_year[1] != next_year[3]:
            #if next_year[2] != next_year[3]:
                #print(next_year)
