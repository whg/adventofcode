"""This is a shocker in terms of performance"""
puzzle = '3113322113'

def generate(s):
    result = ''
    while len(s) != 0:
        start = s[0]
        count = 0
        while count < len(s) and s[count] == start:
            count+= 1

        result+= '%d%s' % (count, start)
        s = s[count:]

    return result

output = puzzle
for i in range(50):
    output = generate(output)
    print(output)
print(len(output))
