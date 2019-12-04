import bisect

def median(items, d, mid):
    if d % 2 == 0:
        return sum(items[mid - 1:mid + 1]) / 2
    else :
        return items[mid]
        
def activityNotifications(expenditure, d):
    n = 0
    mid = int(d / 2)
    sub = sorted(expenditure[:d])
    for i in range(d, len(expenditure)):
        m = 2 * median(sub, d, mid)
        if (expenditure[i] >= m):
            n += 1
        del sub[bisect.bisect_left(sub, expenditure[i - d])]
        bisect.insort(sub, expenditure[i])
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
