def count_subs(array, total):
    return sub(array, total, len(array)-1)

def sub(array, total, i):
    if total == 0:
        return 1
    if total < 1:
        return 0
    if i < 0:
        return 0
    if total < array[i]:
        return sub(array, total, i-1)
    return sub(array, total - array[i], i-1) + sub(array, total, i-1)

def count_subs_dp(array, total):
    map = {}
    return subs_dp(array, total, len(array)-1, map)

def subs_dp(array, total, i, map):
    k = str(total) + ':' + str(i)
    if k in map:
        return map[k]
    if total == 0:
        return 1
    if total < 1:
        return 0
    if i < 0:
        return 0
    if total < array[i]:
        result = subs_dp(array, total, i-1, map)
    else:
        result = subs_dp(array,  total - array[i], i-1, map) + subs_dp(array, total, i-1, map) 
    map[k] = result
    return result

print(count_subs([2,4,6,10], 16))
print(count_subs([2,4,6,10], 6))
print(count_subs([2,4,6,10], 8))

print('\n')

print(count_subs_dp([2,4,6,10], 16))
print(count_subs_dp([2,4,6,10], 6))
print(count_subs_dp([2,4,6,10], 8))