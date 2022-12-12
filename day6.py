data = open('puzzles/input1206.txt')

datastream = data.readline().strip()

for i in range(len(datastream)-13):
    message = datastream[i:i+14]
    cnt = 0
    for char in message:
        if message.count(char) == 1:
            cnt += 1
    if cnt == 14:
        print(i+14)
        print(message)
        break