def print_formatted(number):
    n = len(format(number, 'b'))
    for i in range(1, number + 1): 
        s = str(i)
        sx = format(i, 'x').upper()
        so = format(i, 'o').upper()
        sb = format(i, 'b')
        print(s.rjust(n, ' '), sx.rjust(n, ' '), so.rjust(n, ' '), sb.rjust(n, ' '))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)