def triplets(a, b, c):
    a = distinct(a)
    b = distinct(b)
    c = distinct(c)
    ini = mid = end = triple = 0
    while mid < len(b):
        while ini < len(a) and a[ini] <= b[mid]: ini += 1
        while end < len(c) and c[end] <= b[mid]: end += 1
        triple += ini * end
        mid += 1
    return triple

def distinct(x):
    return list(sorted(set(x)))

if __name__ == '__main__':
    triplets([3, 5, 7],[3, 6],[4, 6, 9])
    triplets([1, 3, 5],[2, 3],[1, 2, 3])
    print(triplets([1, 3, 5, 7],[5, 7, 9],[7, 9, 11, 13]))
    print(triplets([1, 4, 5],[2, 3, 3],[1, 2, 3]))