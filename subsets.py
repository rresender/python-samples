def subsets(nums):
    results = []
    stack = []
    recurse(results, nums, stack, 0)
    return results

def recurse(results, nums, stack, position):
    if position == len(nums):
        results.append(stack.copy())
        return
    stack.append(nums[position])
    recurse(results, nums, stack, position + 1)
    stack.pop()
    recurse(results, nums, stack, position + 1)

print(*subsets([1,2,3]), sep = "\n")