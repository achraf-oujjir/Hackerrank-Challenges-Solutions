def findDigits(n):
    return sum([not bool(n % i) for i in [int(d) for d in str(n) if d != '0']])

n = 106108048 #should return 5
print(findDigits(n))