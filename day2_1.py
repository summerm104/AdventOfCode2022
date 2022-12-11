with open ('puzzles/input1202.txt') as data:
    rounds = []
    for line in data.readlines():
        round = line.strip().split()
        rounds.append(round)
    
    win = {'X': 'C', 'Y': 'A', 'Z': 'B'}
    draw = {'X': 'A', 'Y': 'B', 'Z': 'C'}
    lose = {'X': 'B', 'Y': 'C', 'Z': 'A'}
    score = {'X': 1, 'Y': 2, 'Z':3}

    total_score = 0
    for round in rounds:
        total_score += score[round[1]]
        if round[0] == win[round[1]]:
            total_score += 6
        elif round[0] == draw[round[1]]:
            total_score += 3
    
    print(total_score)
