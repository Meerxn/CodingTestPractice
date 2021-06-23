class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        prev = nums[0]
        found = 0
        i = 0 
        while(i<len(nums)-1):
            if nums[i+1] != nums[i]:
                return nums[i]
            else:
                i = i + 2
        return nums[i]
