

def visit(direction, current):
    x, y = current
    if direction == 'v':
        return (x, y-1)
    elif direction == '^':
        return (x, y+1)
    elif direction == '>':
        return (x+1, y)
    elif direction == '<':
        return (x-1, y)

def traverse(route, return_raw=False):
    current_place = (0, 0)
    visited = set([current_place])

    for c in route:
        next_place = visit(c, current_place)
        visited.add(next_place)
        current_place = next_place

    if return_raw:
        return visited
    else:
        return len(visited)

assert(traverse('>') == 2)
assert(traverse('^>v<') == 4)
assert(traverse('^v^v^v^v^v') == 2)

with open('data/day3.data') as f:
    d = f.read()

print(traverse(d))

def dual_traverse(route):

    santa = traverse(route[::2], True)
    robot = traverse(route[1::2], True)
    return len(santa | robot)


assert(dual_traverse('>v') == 3)
assert(dual_traverse('^>v<') == 3)
assert(dual_traverse('^v^v^v^v^v') == 11)

print(dual_traverse(d))
