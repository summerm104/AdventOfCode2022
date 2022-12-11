stacks = {
    '1': ['Z', 'P', 'M', 'H', 'R'],
    '2': ['P', 'C', 'J', 'B'],
    '3': ['S', 'N', 'H', 'G', 'L', 'C', 'D'],
    '4': ['F', 'T', 'M', 'D', 'Q', 'S', 'R', 'L'],
    '5': ['F', 'S', 'P', 'Q', 'B', 'T', 'Z', 'M'],
    '6': ['T', 'F', 'S', 'Z', 'B', 'G'],
    '7': ['N', 'R', 'V'],
    '8': ['P', 'G', 'L', 'T', 'D', 'V', 'C', 'M'],
    '9': ['W', 'Q', 'N', 'J', 'F', 'M', 'L']
}

data = [line.strip() for line in open('puzzles/input1205.txt').readlines()]

steps = []
for item in data:
    item = item.split()
    step = [int(item[1]), item[3], item[5]]
    steps.append(step)

for step in steps:
    n = step[0]
    s_from = step[1]
    s_to = step[2]

    s_move = stacks[s_from][-n:]
    stacks[s_from] = stacks[s_from][:len(stacks[s_from])-n]
    stacks[s_to] = stacks[s_to] + s_move

values = list(stacks.values())
message = ''.join([crates[-1] for crates in values])

print(message)
