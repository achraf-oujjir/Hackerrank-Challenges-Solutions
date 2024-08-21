def findDigits(n):
    return len([n % i for i in [int(d) for d in str(n) if d != '0']])

n = 12
print(findDigits(n))