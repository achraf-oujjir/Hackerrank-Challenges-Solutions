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

def optimizedProductExceptSelf(nums: list[int]) -> list[int]:
    res = [1] * len(nums)
    l = 1
    for i in range(len(nums)):
        res[i] = l
        l *= nums[i]
    
    r = 1
    for i in range(len(nums)-1, -1, -1):
        res[i] *= r
        r *= nums[i]
    
    return res

def myProductExceptSelf(nums:list[int]) -> list[int]:
    res, l, r = [1] * len(nums), 1, 1
    for i in range(len(nums)):
        res[i] *= l
        l *= nums[i]
        j = -i - 1
        res[j] *= r
        r *= nums[j]
    return res

nums = [1,2,3,4]
print(productExceptSelf(nums))
