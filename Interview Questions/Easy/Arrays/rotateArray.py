class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k == 0:
            return
        n = len(nums)
        nums[:] = nums[::-1]
        nums[0:k] = nums[k-n-1:-n-1:-1] 
        nums[k:n] = nums[n-1:k-1:-1]
                
