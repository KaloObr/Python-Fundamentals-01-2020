cards = input().split(' ')

team_a_playes = [str(_) for _ in range(1, 12)]
team_b_playes = [str(_) for _ in range(1, 12)]
terminated = False

for card in cards:
    team, value = card.split('-')

    if team == "A":
        if value in team_a_playes:
            team_a_playes.remove(value)

    elif team == 'B':
        if value in team_b_playes:
            team_b_playes.remove(value)

    if len(team_a_playes) < 7 or len(team_b_playes) < 7:
        terminated = True
        break

print(f'Team A - {len(team_a_playes)}; Team B - {len(team_b_playes)}')

if terminated:
    print("Game was terminated")

