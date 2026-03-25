class Solution(object):
    def maxProfit(self, prices):
        if not prices or len(prices) < 2:
            return 0
        i=0
        min_pur = prices[0]
        largest = 0
        while i<len(prices):
            if (prices[i] < min_pur):
                min_pur = prices[i]
                
            if (prices[i] - min_pur) > largest:
                largest = prices[i] - min_pur
            i+=1
        if largest == 0 or largest <0:
            return 0
        return largest
        
        
s= Solution()
print(s.maxProfit([7,6,4,3,1]))