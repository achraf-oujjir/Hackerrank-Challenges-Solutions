def majorityElement(nums: list[int]) -> int:
    dico = {i: nums.count(i) for i in nums}
    return max(dico, key=dico.get)

def betterMajorityElement(nums: list[int]) -> int:
    candidate = nums[0]
    count = 0
    for n in nums:
        if candidate == n: count += 1
        else:
            if count > 0: count -= 1
            else: candidate = n
    return candidate

nums = [2, 2, 1, 1, 1, 2, 2]
print(betterMajorityElement(nums))