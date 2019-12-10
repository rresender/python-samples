if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(sorted(set(arr)))
    n = len(arr)
    if n >= 2:
        n -= 2
    else:
        n -= 1
    print(arr[n])