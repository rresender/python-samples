from itertools import combinations_with_replacement

if __name__ == '__main__':
    s, n =input().split(' ')
    s = sorted(s)
    ret = []
    for x in list(combinations_with_replacement(s, int(n))):
        e = ''.join(x) 
        ret.append(e)
    [print(i) for i in ret]     
