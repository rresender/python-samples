
from statistics import median

def activityNotifications(expenditure, d):
    n = 0
    i = 0
    for x in range(d, len(expenditure)):
        m = median(expenditure[i:d+i])
        if expenditure[x] >= (2 * m):
            n += 1
        i += 1
    return n

if __name__ == '__main__':
    
    # opt = "5 3"
    # values = "10 20 30 40 50"

    opt = "9 5"
    values = "2 3 4 2 3 6 8 4 5"

    # opt = "5 6"
    # values = "1 2 3 4 4"

    nd = opt.split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, values.rstrip().split()))

    result = activityNotifications(expenditure, d)

    print(str(result) + '\n')
