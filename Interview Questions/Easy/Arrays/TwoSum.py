class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums1 = sorted(nums)
        left = 0
        right = len(nums1) -1
        x = {}
        res = [0,0]
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in x:
                res[0] = i
                res[1] = x[diff]
                return res
            else:
                x[nums[i]] = i
                
        
        