def hammingWeight(n: int) -> int:
    ans = 0
    
    while n:
        ans += 1
        n &= n-1
    
    return ans

n = 11 # should return 3
print(hammingWeight(n))
