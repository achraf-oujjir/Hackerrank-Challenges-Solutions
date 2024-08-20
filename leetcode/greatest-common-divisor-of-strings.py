from math import gcd

def gcdOfStrings(str1: str, str2: str) -> str:
    len1, len2 = len(str1), len(str2)

    def valid(k):
        if len1 % k or len2 % k:
            return False
        n1, n2 = len1 // k, len2 // k
        base = str1[:k]
        return str1 == n1 * base and str2 == n2 * base

    for i in range(min(len(str1), len(str2)), 0, -1):
        if valid(i):
            return str1[:i]
    return ""


def pythonicGcdOfStrings(str1: str, str2: str) -> str:
    if str1+str2 != str2+str2: return ''
    
    max_length = gcd(len(str1), len(str2))
    return str1[:max_length]


str1 = "ABCABC"
str2 = "TK"
print("This is the gcd: ")
print(gcdOfStrings(str1, str2))
