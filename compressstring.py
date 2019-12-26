if __name__ == '__main__':
    arr = input()
    n = len(arr)
    c = 1
    for i in range(n-1):
        if arr[i] == arr[i+1]:
            c += 1
        else:
            print((c, int(arr[i])), end=' ') 
            c = 1
    print((c, int(arr[n-1])), end=' ') 