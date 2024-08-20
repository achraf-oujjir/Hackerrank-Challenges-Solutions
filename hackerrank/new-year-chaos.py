def minBribes(q: list[int]) -> int:
    moves = 0
    flag = False
    q = [p-1 for p in q]
    
    for i, p in enumerate(q):
        if p-i > 2: flag = True
        
        for j in range(max(p-1, 0), i):
            if q[j] > p: moves += 1
    print(moves)
    if flag: print("Too chaotic")

q = [2, 5, 1, 3, 4]
minBribes(q)
