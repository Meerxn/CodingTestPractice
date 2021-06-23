class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        kth = 1
        prev = 0
        for i in range(1,len(nums)):
            if (nums[prev] < nums[i]):
                nums[kth] = nums[i]
                prev = kth
                kth+=1
        return kth
                
                  
        
                
        