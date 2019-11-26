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

print(count_subs([2,4,6,10], 16))
print(count_subs([2,4,6,10], 6))
print(count_subs([2,4,6,10], 8)) 
    
    