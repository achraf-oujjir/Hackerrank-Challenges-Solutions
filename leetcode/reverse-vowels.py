def reverseVowels(s: str) -> str:
    vowels = "AaEeIiOoUu"
    v = list()
    result = list(s)
    for i, c in enumerate(s):
        if c in vowels: v.append((i, c))
    for j, t in enumerate(v):
        result[t[0]] = v[len(v) - j - 1][1]
    return ''.join(result)

def optimizedReverseVowels(s: str) -> str:
    word = list(s)
    left = 0
    right = len(word) - 1
    vowels = "AaEeIiOoUu"
    
    while left < right:
        while left < right and word[left] not in vowels:
            left += 1
        
        while left < right and word[right] not in vowels:
            end -= 1
        
        word[left], word[right] = word[right], word[left]
        left += 1
        right -= 1
    return "".join(word)
    
    

s = "hello"
print(optimizedReverseVowels(s))