def twoSum(nums: list[int], target: int) -> list[int]:
    dico = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in dico: return [dico[diff], i]
        dico[n] = i
        
    dico = {} # This dico has numbers as keys with their indexes as values
    for i, n in enumerate(nums):
        diff = target - n
        if diff in dico: return [dico[diff], ]


