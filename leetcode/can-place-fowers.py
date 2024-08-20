def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    # To solve this problem, we'll need to determine the conditions to be able to place a flower:
    # We need to have three consecutive 0's to place 1 flower.
    # ex: [1, 0, 0, 0, 1, 0]
    # We also have two other cases: if we have 2 0's in the start or end of the list.
    # let's make a function that returns the length of the sequence from an index
    
    valid_plots = 0
    left = False
    
    def sequence(bed: list[int], start: int) -> int:
        seq = 0
        for p in bed[start:]:
            if p == 1: break
            seq += 1
        return seq
    
    new = flowerbed[:]
    
    if sequence(new, 0) > 2:
        valid_plots +=1
        left = True
        new[0] = 1

    if sequence(new, len(new)-2) == 2:
        valid_plots += 1
        new[-1] = 1
    
    starting = 1 if left else 0
    for i in range(starting, len(new)-2):
        if sequence(new, i) >= 3:
            new[i+1] = 1
            valid_plots += 1
    
    print(new)
    print(valid_plots)
    return valid_plots >= n

def optimizedWay(flowerbed: list[int], n: int) -> bool:
    count = 0
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0:
            empty_left = (i==0) or (flowerbed[i-1] == 0)
            empty_right = (i==len(flowerbed)-1) or (flowerbed[i+1] == 0)
            if empty_left and empty_right:
                flowerbed[i] = 1
                count += 1
    return count >= n
    
    

flowerbed = [1,0,0,0,1]
n = 2
print(canPlaceFlowers(flowerbed, n))
