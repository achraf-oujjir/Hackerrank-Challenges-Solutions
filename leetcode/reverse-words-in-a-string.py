def reverseWords(s: str) -> str:
    return " ".join(s.split()[::-1])

s = "the sky is blue"
print(reverseWords(s))