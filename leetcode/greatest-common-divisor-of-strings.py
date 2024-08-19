def gcdOfStrings(str1: str, str2: str) -> str:
    small = str2 if len(str2) < len(str1) else str1
    big = str1 if len(str1) > len(str2) else str2
    gcd = small
    while gcd != '':
        if len(big) % len(gcd) == 0:
            k = len(big) // len(gcd)
            if big == k*gcd: return gcd
        gcd = gcd[:-1]
    return ''


str1 = "ABCABC"
str2 = "TK"
print("This is the gcd: ")
print(gcdOfStrings(str1, str2))
