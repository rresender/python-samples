def num_ways(n):
    if n == 0 or n == 1:
        return 1
    return num_ways(n-1)+num_ways(n-2)

def num_ways_dp(n):
    if n == 0 or n == 1:
        return 1
    nums = [0 for x in range(n+1)]
    nums[0] = nums[1] = 1
    for i in range(2, len(nums)):
        nums[i] = nums[i-1] + nums[i-2]
    return nums[n]

print(num_ways(5))
print(num_ways_dp(5))