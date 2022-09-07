class Solution:
    def maxProfit(self, prices) -> int:
        max_profit = 0
        sell = 0 
        buy = None
        profit = 0
        
        for i in prices:
            if buy == None:
                buy = i
            elif i > buy and i > sell:
                sell = i
                profit = i-buy
            elif i < buy:
                buy = i
                sell = 0
                profit = 0
            
            if profit > max_profit:
                max_profit = profit
        
        return max_profit
    
    def maxProfit2(self, prices: List[int]) -> int: #after removing redundant 'sell' variable, this code ran faster on leetcode
        max_profit = 0
        buy = prices[0]
        
        for i in prices:
            if i > buy:
                profit = i-buy
            else:
                buy = i
                profit = 0
            
            if profit > max_profit:
                max_profit = profit
        
        return max_profit

l1 = [3,3,5,0,0,3,1,4]
l2 = [2,1,2,1,0,1,2]

test = Solution()
print(test.maxProfit(l1))
print(test.maxProfit(l2))