with open('data/1.data') as f:
    s = f.read()

print(sum(map(lambda e: 1 if e == '(' else -1, s)))


sum = 0
for i, c in enumerate(s):
    if c == '(':
        sum+= 1
    elif c == ')':
        sum-= 1
    if sum == -1:
        print(i+1)
        break
        




    

