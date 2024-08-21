def twoSum(nums: list[int], target: int) -> list[int]:
    dico = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in dico: return [dico[diff], i]
        dico[n] = i