with open ('puzzles/input1202.txt') as data:
    rounds = []
    for line in data.readlines():
        round = line.strip().split()
        rounds.append(round)
    
    win = {'A': 'B', 'B': 'C', 'C': 'A'}
    draw = {'A': 'A', 'B': 'B', 'C': 'C'}
    lose = {'A': 'C', 'B': 'A', 'C': 'B'}
    score = {'A': 1, 'B': 2, 'C': 3}

    total_score = 0
    for round in rounds:
        # 'X' means lose
        if round[1] == 'X':
            total_score += score[lose[round[0]]]
        elif round[1] == 'Y':
            total_score += 3
            total_score += score[draw[round[0]]]
        else:
            total_score += 6
            total_score += score[win[round[0]]]

    print(total_score)
        
    
    