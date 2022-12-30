with open('input.txt', 'r') as file:
    data = file.readline().strip()

for index in range(len(data) - 4):
    split = data[index:index+4]
    if len(set(split)) == 4:
        print(f'Part 1: {index + 4}')
        break

for index in range(len(data) - 14):
    split = data[index:index+14]
    if len(set(split)) == 14:
        print(f'Part 2: {index + 14}')
        break