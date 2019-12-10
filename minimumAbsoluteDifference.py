import sys

def minimumAbsoluteDifference(arr):
    diffs = []
    arr = sorted(arr)
    for i in range(len(arr)-1):
        diffs.append(abs(arr[i]-arr[i+1]))
    return min(diffs)

print(minimumAbsoluteDifference([-2, 2, 4]))
print(minimumAbsoluteDifference([3, -7, 0]))
print(minimumAbsoluteDifference([-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]))
print(minimumAbsoluteDifference([1, -3, 71, 68, 17]))