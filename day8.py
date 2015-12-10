import re

with open('data/8.data') as f:
    lines = f.readlines()

def part_a(l):
    l = l.strip()
    l2 = l[1:-1]
    l2 = re.sub(r'\\x[0-9a-f]{2}', '_', l2)
    l2 = re.sub(r'\\"', '"', l2)
    l2 = re.sub(r'\\\\', '_', l2)
    return (len(l), len(l2))

a, b = list(zip(*list(map(part_a, lines))))
print(sum(a) - sum(b))

def part_b(l):
    l = l.strip()
    l2 = l
    l2 = re.sub(r'(\\")', '____', l2)
    l2 = re.sub(r'"', '__', l2)
    l2 = re.sub(r'(\\x[0-9a-f]{2})', '_____', l2)
    l2 = re.sub(r'\\', '__', l2)

    return (len(l), len(l2) + 2)

a, b = list(zip(*list(map(part_b, lines))))
print(sum(b) - sum(a))
