import textwrap

def wrap(string, max_width):
    ret = ''
    n = len(string) // max_width
    while n >= 0: 
        ret += string[:max_width] + '\n'
        string = string[max_width:]
        n -= 1
    return ret

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)