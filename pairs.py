
def pairs(k, arr):
    list = set(arr)
    count_pairs = 0
    for val in arr:
        if (val + k) in list:
            count_pairs += 1
    return count_pairs
    
print(pairs(2, [1, 5, 3, 4, 2]))
print(pairs(1, [1, 2, 3, 4]))