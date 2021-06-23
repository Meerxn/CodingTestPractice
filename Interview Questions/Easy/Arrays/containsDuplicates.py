class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        prev = nums[0]
        for i in range(1,len(nums)):
            curr = nums[i]
            if curr == prev:
                return True
            else:
                prev = curr
        return False
        