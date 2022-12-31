from collections import defaultdict
from functools import reduce

with open('input.txt', 'r') as file:
    data = [line.strip() for line in file.readlines()]

def is_visible(j: int, i: int):
    row = data[j]
    for di in range(len(row)):
        if di == i:
            return 1
        if row[di] >= row[i]:
            break
    for di in range(len(row) - 1, 0, -1):
        if di == i:
            return 1
        if row[di] >= row[i]:
            break
    for dj in range(len(data)):
        if dj == j:
            return 1
        if data[dj][i] >= data[j][i]:
            break
    for dj in range(len(data) - 1, 0, -1):
        if dj == j:
            return 1
        if data[dj][i] >= data[j][i]:
            break
    return 0



total = 0

total += 2 * len(data[0])
total += 2 * (len(data) - 2)

for j in range(1, len(data) - 1):
    for i in range(1, len(data[0]) - 1):
        total += is_visible(j, i)

print(f'Part 1: {total}')


def count_visible_trees(j: int, i: int):
    trees = {0: 0, 1: 0, 2: 0, 3: 0}
    for di in range(i + 1, len(data[j])):
        if data[j][di] >= data[j][i]:
            trees[0] += 1
            break
        trees[0] += 1
    for di in range(i - 1, -1, -1):
        if data[j][di] >= data[j][i]:
            trees[1] += 1
            break
        trees[1] += 1
    for dj in range(j + 1, len(data)):
        if data[dj][i] >= data[j][i]:
            trees[2] += 1
            break
        trees[2] += 1
    for dj in range(j - 1, -1, -1):
        if data[dj][i] >= data[j][i]:
            trees[3] += 1
            break
        trees[3] += 1

    return reduce(lambda x, y: x * y,list(trees.values()))


total2 = []

for j in range(1, len(data) - 1):
    for i in range(1, len(data[0]) - 1):
        total2.append(count_visible_trees(j, i))

print(f'Part 2: {max(total2)}')