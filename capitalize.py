def solve(s):
    names = s.split(' ')
    ret = []
    for n in names:
        if (len(n) == 0 or n[0].isdigit()):
            ret.append(n)
        else:    
            ret.append(n[0].upper()+n[1:])
    return ' '.join(ret)

print(solve('hello   world  lol'))