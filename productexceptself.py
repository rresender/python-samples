def product_except_self(nums):
        n = len(nums)

        results = [0] * n
        
        left = 1

        for i in range(n):
            if i > 0:
                left *= nums[i - 1]

            results[i] = left
        
        right = 1
        
        for i in range(n-1, -1, -1):
            if i < n - 1:
                right *= nums[i + 1]

            results[i] *= right
        
        return results

print(product_except_self([1,2,3,4]))