import re
from itertools import chain, permutations

regex = re.compile(r'([A-Za-z]+) to ([A-Za-z]+) = (\d+)')

def toIndex(s, e):
    return '-'.join(sorted([s, e]))

def parse(l):
    start, end, dist = re.search(regex, l).groups()
    return (toIndex(start, end), int(dist))

with open('data/9.data') as f:
    lines = f.readlines()

distances = dict(map(parse, lines))
places = set(chain(*[k.split('-') for k in distances.keys()]))

    
def length(sequence):
    global distances
    l = 0
    for start, end in zip(sequence[::], sequence[1::]):
        l+= distances[toIndex(start, end)]
    return l
    
    
print(min(map(length, permutations(places))))
print(max(map(length, permutations(places))))
