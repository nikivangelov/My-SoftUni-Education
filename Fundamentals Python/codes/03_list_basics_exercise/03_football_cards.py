given_red_cards = input().split()
all_sent_off_players =[]
sent_off_A_team = []
sent_off_B_team = []
count_A_team = 11
count_B_team = 11
terminated_game = False

for current_red_card in range(len(given_red_cards)):
    if 'A' in given_red_cards[current_red_card]:
        if given_red_cards[current_red_card] in sent_off_A_team:
            continue

        sent_off_A_team.append(given_red_cards[current_red_card])
        count_A_team -= 1
        if count_A_team < 7:
            terminated_game = True
            break
    elif 'B' in given_red_cards[current_red_card]:
        if given_red_cards[current_red_card] in sent_off_B_team:
            continue
        sent_off_B_team.append(given_red_cards[current_red_card])
        count_B_team -= 1
        if count_B_team < 7:
            terminated_game = True
            break

print(f"Team A - {count_A_team}; Team B - {count_B_team}")
if terminated_game:
    print("Game was terminated")