def maxProfit(prices: list[int]) -> int:
    l, r = 0, 1
    maxP = 0
    
    while r < len(prices):
        if prices[l] < prices[r]: #if profitable
            profit = prices[r] - prices[l]
            maxP = max(profit, maxP)
        
        else: #if not profitable
            l = r
        r += 1
    return maxP

def optimizedMaxProfit(prices: list[int]) -> int:
    profit = 0
    buy = prices[0]

    for price in prices:
        buy = min(buy, price)
        profit = max(profit, price - buy)
    return profit




prices = [7,1,5,3,6,4] # should return 5
print(optimizedMaxProfit(prices))