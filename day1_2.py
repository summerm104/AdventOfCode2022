with open('puzzles/input1201.txt') as data:
    calorie_list = [line.strip() for line in data]
    elf = []
    elves = []
    for calorie in calorie_list:
        if calorie != '':
            calorie = int(calorie)
            elf.append(calorie)
        else:
            elves.append(elf)
            elf = []
    res = []
    for elf in elves:
        res.append(sum(elf))
    
    res.sort(reverse=True)

    top_three = sum(res[0:3])

    print(top_three)
    