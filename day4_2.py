with open('puzzles/input1204.txt') as data:
    assignments = [line.strip().split(',') for line in data.readlines()]
    
    elf_assignments = []

    # map()
    for assignment in assignments:
        assignment_1 = [int(n) for n in assignment[0].split('-')]
        assignment_2 = [int(n) for n in assignment[1].split('-')]

        elf_assignments.append([assignment_1, assignment_2])

    overlap = 0
    overlap_copy = []

    for assign_group in elf_assignments:
        if assign_group[0][0] > assign_group[1][1] or assign_group[0][1] < assign_group[1][0]:
            pass
        else:
            overlap += 1
            
    print(overlap)