import copy
from functools import reduce

with open('day11/input.txt', 'r') as file:
    data = file.read().split('\n\n')

class Monkey:
    def __init__(self, id: str, items, operation, divisor, monkey_t, monkey_f):
        self.id: str = id
        self.items = items
        self.operation = operation
        self.divisor = divisor
        self.monkey_t = monkey_t
        self.monkey_f = monkey_f
        self.inspections = 0

    def __repr__(self):
        return f'{self.id} {self.items} {self.operation}'

    def begin(self, monkies, part1, div=0):
        for _ in range(len(self.items)):
            self.throw(monkies, part1, div)

    def throw(self, monkies, part1, div):
        item = self.items.pop(0)
        self.inspections += 1
        operation = self.operation.copy()
        for i in range(len(operation)):
            if operation[i] == 'old':
                operation[i] = item
        
        if operation[1] == '*':
            item = operation[0] * operation[2]
        else:
            item = operation[0] + operation[2]

        if part1:
            item = item // 3
        else:
            item = item % div

        if item % self.divisor == 0:
            monkies[self.monkey_t].receive(item)
        else:
            monkies[self.monkey_f].receive(item)

    def receive(self, item):
        self.items.append(item)

monkies = []
index = 0

for monkey_list in data:
    monkey = [line.lstrip() for line in monkey_list.split('\n')]

    items = [int(num) for num in monkey[1][16:].split(',')]
    operation = [op for op in monkey[2][17:].split(' ')]
    for i in range(len(operation)):
        if operation[i].isnumeric():
            operation[i] = int(operation[i])
    divisor = int(monkey[3][19:])
    monkey_t = int(monkey[4][25:])
    monkey_f = int(monkey[5][26:])
    
    monkies.append(Monkey(index, items, operation, divisor, monkey_t, monkey_f))
    index += 1

monkies1 = copy.deepcopy(monkies)

for i in range(20):
    for monkey in monkies1:
        monkey.begin(monkies1, True)

inspections = []

for monkey in monkies1:
    inspections.append(monkey.inspections)

max1 = max(inspections)
inspections.remove(max1)
max2 = max(inspections)

print(f'Part 1: {max1 * max2}')

monkies2 = copy.deepcopy(monkies)

mod = reduce(lambda x, y: x * y, [m.divisor for m in monkies2])

for i in range(10000):
    for monkey in monkies2:
        monkey.begin(monkies2, False, mod)

inspections2 = []

for monkey in monkies2:
    inspections2.append(monkey.inspections)

max1_2 = max(inspections2)
inspections2.remove(max1_2)
max2_2 = max(inspections2)

print(f'Part 2: {max1_2 * max2_2}')


