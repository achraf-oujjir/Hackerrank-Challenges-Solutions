from collections import Counter

def frequencySort(nums: list[int]) -> list[int]:
    count = Counter(nums)
    nums.sort(key=lambda n: (count[n], -n))
    return nums

#nums = [1,1,2,2,2,3]
nums = [2,3,1,3,2]
print(frequencySort(nums))
