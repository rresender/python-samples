import re

def get_pairs(s):
    pairs = set()
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            pairs.add((s[i], s[j]))
    return pairs

def alternate(s):
    maximum = 0
    words = distinct(s)
    pairs = get_pairs(words)
    strings = list(s)
    for pair in pairs:
        temp = s
        for x in strings:
            if x not in pair:
                temp = temp.replace(x, '')
        if checkalternate(temp):
            maximum = max(len(temp), maximum)        
    return maximum

def distinct(x):
    return list(sorted(set(x)))

def checkalternate(s):
    if re.match(r"^([a-z])(?!\1)([a-z])(?:\1\2)*\1?$", s) == None:
        return False
    return True

print(alternate('beabeefeab'))
print(alternate('abaacdabd'))
print(alternate('asdcbsdcagfsdbgdfanfghbsfdab'))

