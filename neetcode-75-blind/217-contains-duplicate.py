def containsDuplicate(nums: list[int]) -> bool:
    return not len(nums) == len(set(nums))

nums = [1,1,1,3,3,4,3,2,4,2]
print(containsDuplicate(nums))
