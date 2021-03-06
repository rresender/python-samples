# linear sorted version
def has_pair_with_sum(data, sum):
    low = 0
    high = len(data) - 1
    while(low < high):
        result = data[low] + data[high]
        print(result)
        if sum == result:
            return True
        elif result < sum:
            low = low + 1 
            print('low')
        else:
            high = high - 1 
            print('high')
    return False

# linear sorted version
def has_pair_with_sum_non_sorted(data, sum):
    list = set()
    for val in data:
        if val in list:
            return True
        list.add(sum - val)
    return False

sum = 15
data = [1, 2, 3, 4, 4, 5, 10]
print(has_pair_with_sum(data, sum))
data = [10, 5, 1, 2, 3, 4, 4]
print(has_pair_with_sum_non_sorted(data, sum))