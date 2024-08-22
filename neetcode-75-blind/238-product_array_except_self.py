def productExceptSelf(nums: list[int]) -> list[int]:
    n = len(nums)
    l, r = [1] * n, [1] * n
    l_mult, r_mult = 1, 1
    
    for i in range(n):
        j = -i - 1
        l[i], r[j] = l_mult, r_mult  
        l_mult *= nums[i]
        r_mult *= nums[j]
    
    return [a * b for a, b in zip(l, r)]

nums = [1,2,3,4]
print(productExceptSelf(nums))
