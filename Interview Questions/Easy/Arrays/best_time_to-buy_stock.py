class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minVal =0
        maxVal = 0
        prof = 0
        index = 0
        while(index < len(prices)-1):
            while (index<len(prices)-1 and prices[index+1]<= prices[index] ):
                index+=1
                minVal =  prices[index]
            while (index<len(prices)-1 and prices[index+1] > prices[index]):
                index+=1
                maxVal = prices[index]
            prof += maxVal-minVal
                
                
        return prof
        