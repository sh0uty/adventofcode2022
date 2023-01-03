import nographs as nog

with open('day12/input.txt', 'r') as file:
    data = [line.strip() for line in file.readlines()]

start = 'S'

a = nog.Array(data)

limits = a.limits()
moves = nog.Position.moves()

def elevation(c):
    return ord({"S": "a", "E": "z"}.get(c, c))

def next_vertex(p: nog.Position, _):
    for p2 in p.neighbors(moves, limits):
        if elevation(a[p2]) <= elevation(a[p]) + 1:
            yield p2

s = a.findall(start)
e = a.findall('E')[0]

t = nog.TraversalBreadthFirst(next_vertex).start_from(start_vertices=s)
t.go_to(e)

print(f'Part 1: {t.depth}')

s = a.findall('a')

t = nog.TraversalBreadthFirst(next_vertex).start_from(start_vertices=s)
t.go_to(e)

print(f'Part 2: {t.depth}')

