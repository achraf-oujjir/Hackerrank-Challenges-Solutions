def kidsWithCandies( candies: list[int], extraCandies: int) -> list[bool]:
    return list(map(lambda x: x+extraCandies >=  max(candies), candies))

candies = [2,3,5,1,3]
extraCandies = 3
print(kidsWithCandies(candies, extraCandies))
