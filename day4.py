from hashlib import md5
from time import time
from sys import stdout

def a(input, startswith='00000'):

    counter = 1
    start = time()
    timing_gap = 5000
    
    while True:
        h = md5(bytes(input + str(counter), 'utf8')).hexdigest()
        if h.startswith(startswith):
            break

        if counter % timing_gap == 0:
            now = time()
            stdout.write('\r%d: %s last tries took %fs' % (counter, timing_gap, now - start))
            start = now

        counter+= 1

    print()
    return counter

assert(a('abcdef') == 609043)
assert(a('pqrstuv') == 1048970)

print(a('yzbqklnj'))
print(a('yzbqklnj', '000000'))

