import re

def nice(s):

    vowels = 'aeiou'
    found_vowels = 0
    for vowel in vowels:
        found_vowels+= len(re.findall(vowel, s))

        if found_vowels >= 3:
            break

    if found_vowels < 3:
        return False

    if not re.search(r'([a-z])\1', s):
        return False

    if re.search('(ab)|(cd)|(pq)|(xy)', s):
        return False

    return True


assert(nice('ugknbfddgicrmopn') == True)
assert(nice('aaa') == True)
assert(nice('jchzalrnumimnmhp') == False)
assert(nice('haegwjzuvuyypxyu') == False)
assert(nice('dvszwmarrgswjxmb') == False)

with open('data/5.data') as f:
    lines = f.readlines()

print(sum(map(nice, lines)))

def nice2(s):

    pairs = map(lambda e: ''.join(e), zip(s[::], s[1::]))
    #doubles = re.findall(r'(:?[a-z])\1', s)
    has_double_pair = False

    for pair in pairs:
        first_match = re.search(pair, s)
        if first_match:
            span = first_match.span()
            temps = s[:span[0]]
            if re.search(pair, s[:span[0]]):
                has_double_pair = True
            elif re.search(pair, s[span[1]:]):
                has_double_pair = True
        # if len(re.findall(pair, s)) >= 2:
        #     has_double_pair = True
        #     break

    if not has_double_pair:
        print('no double pair')
        return False

    if re.search(r'([a-z])[a-z]\1', s):
        return True

    return False

assert(nice2('qjhvhtxzqqjkmpb') == True)
assert(nice2('xxyxx') == True)
assert(nice2('uurcxstgmygtbstg') == False)
assert(nice2('ieodomkazucvgmuy') == False)
assert(nice2('avava') == True)

print(sum(map(nice2, lines)))
