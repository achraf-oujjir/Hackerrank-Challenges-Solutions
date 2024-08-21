def reverseVowels(s: str) -> str:
    vowels = "AaEeIiOoUu"
    v = list()
    result = list(s)
    for i, c in enumerate(s):
        if c in vowels: v.append((i, c))
    for j, t in enumerate(v):
        result[t[0]] = v[len(v) - j - 1][1]
    return ''.join(result)

s = "hello"
print(reverseVowels(s))