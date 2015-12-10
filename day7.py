import re

regex = re.compile(r'([a-z0-9]+)? ?(AND|OR|LSHIFT|RSHIFT|NOT)? ?([a-z0-9]+)? -> ([a-z]+)')

def parse(l):
    r = re.search(regex, l).groups()
    return (r[3], r[:3])

cache = {}
def value(a):
    global cache, data

    if re.search('[a-z]', a):
        try:
            return cache[a]
        except KeyError:
            val = evaluate(data[a])
            cache[a] = val
            return val
    else:
        return int(a)
    
def evaluate(instruction):
    global data
    
    a, operation, b = instruction
    
    if operation == None:
        return value(a)
    elif operation == 'NOT':
        return ~value(b) & (2*16-1)
    elif operation == 'AND':
        return value(a) & value(b)
    elif operation == 'OR':
        return value(a) | value(b)
    elif operation == 'LSHIFT':
        return value(a) << value(b)
    elif operation == 'RSHIFT':
        return value(a) >> value(b)


with open('data/7.data') as f:
    lines = f.readlines()

data = dict(map(parse, lines))

#print(evaluate(data['a']))

data['b'] = ('46065', None, None)
print(evaluate(data['a']))
