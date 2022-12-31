with open('input.txt', 'r') as file:
    data = [line.strip() for line in file.readlines()]

head = [0, 0]
tail = [0, 0]

tail_pos = [[0, 0]]

def is_next(head, tail):
    dx = abs(head[0] - tail[0])
    dy = abs(head[1] - tail[1])
    return max([dx, dy]) < 2


for line in data:
    dir, count = line.split(' ')
    for i in range(int(count)):
        print(dir, count)
        if dir == 'R':
            head[0] += 1
            if not is_next(head, tail):
                tail[0] = head[0] - 1
                tail[1] = head[1]
                tail_pos.append(tail[:])
        elif dir == 'D':
            head[1] -= 1
            if not is_next(head, tail):
                tail[0] = head[0]
                tail[1] = head[1] + 1 
                tail_pos.append(tail[:])
        elif dir == 'L':
            head[0] -= 1
            if not is_next(head, tail):
                tail[0] = head[0] + 1
                tail[1] = head[1]
                tail_pos.append(tail[:])
        elif dir == 'U':
            head[1] += 1
            if not is_next(head, tail):
                tail[0] = head[0]
                tail[1] = head[1] - 1
                tail_pos.append(tail[:])

print(len(set([tuple(x) for x in tail_pos])))