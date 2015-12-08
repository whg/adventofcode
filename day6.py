import re
import numpy as np

class Instruction():
    def __init__(self, line):
        bc, tc = re.findall('[0-9]+,[0-9]+', line)
        
        bcx, bcy = bc.split(',')
        tcx, tcy = tc.split(',')

        self.start = slice(int(bcx), int(tcx)+1, 1)
        self.end = slice(int(bcy), int(tcy)+1, 1)

        actions = ['on', 'off', 'toggle']
        for action in actions:
            if action in line:
                self.action = action
                
    def __repr__(self):
        return '%s: %s -> %s' % (self.action, self.start, self.end)
        

with open('data/6.data') as f:
    lines = f.readlines()

instructions = map(Instruction, lines)

def a(instructions):
    dim = (1000, 1000)
    grid = np.zeros(dim)
    
    for i in instructions:

        if i.action == 'on':
            grid[i.start, i.end] = 1
        elif i.action == 'off':
            grid[i.start, i.end] = 0
        elif i.action == 'toggle':
            fresh = np.zeros(dim)
            fresh[i.start, i.end] = 1
            grid += fresh
            grid %= 2

    return np.sum(grid)


assert(a([Instruction('turn on 0,0 through 999,999')]) == 1000000)

#print(a(instructions))

def b(instructions):
    dim = (1000, 1000)
    grid = np.zeros(dim)
    
    for i in instructions:
        if i.action == 'on':
            grid[i.start, i.end]+= 1
        elif i.action == 'off':
            grid[i.start, i.end]-= 1
            below = grid < 0
            grid[below] = 0
        elif i.action == 'toggle':
            grid[i.start, i.end]+= 2

    return np.sum(grid)

assert(b([Instruction('turn on 0,0 through 0,0')]) == 1)
assert(b([Instruction('toggle on 0,0 through 999,999')]) == 2000000)

print(b(instructions))
