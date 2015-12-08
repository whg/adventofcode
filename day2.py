


def parse(l):
    return [int(c) for c in l.strip().split('x')]

def area(l, w, h):
    return 2*l*w + 2*w*h + 2*h*l

def paper(dim):
    e1, e2 = sorted(dim)[:2]

    return area(*dim) + e1 * e2
    
assert(paper(parse("2x3x4")) == 58)
assert(paper(parse("1x1x10")) == 43)

with open('data/2.data') as f:
    lines = f.readlines()
boxes = [parse(l) for l in lines]

print(sum(map(paper, boxes)))


def ribbon(dim):
    e1, e2 = sorted(dim)[:2]
    x, y, z = dim
    return x * y * z + e1 + e1 + e2 + e2

assert(ribbon(parse("2x3x4")) == 34)
assert(ribbon(parse("1x1x10")) == 14)

print (sum(map(ribbon, boxes)))
