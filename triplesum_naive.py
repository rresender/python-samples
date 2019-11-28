def triplets(a, b, c):
    ret = 0
    a = distinct(a)
    b = distinct(b)
    c = distinct(c)
    for i in a:
        for j in b:
            for z in c:
                if i <= j and j >= z:
                    ret += 1
    return ret

def distinct(x):
    return list(sorted(set(x)))

if __name__ == '__main__':
    # triplets([3, 5, 7],[3, 6],[4, 6, 9])
    # triplets([1, 3, 5],[2, 3],[1, 2, 3])
    # print(triplets([1, 3, 5, 7],[5, 7, 9],[7, 9, 11, 13]))
    print(triplets([1, 4, 5],[2, 3, 3],[1, 2, 3]))