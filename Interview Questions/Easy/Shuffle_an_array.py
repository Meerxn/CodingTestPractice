import random
import copy
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = list(nums)
        
        

    def reset(self) -> List[int]:
        return self.nums
        """
        Resets the array to its original configuration and return it.
        """
        

    def shuffle(self) -> List[int]:
        x = random.sample(self.nums,len(self.nums))
        return x

        """
        Returns a random shuffling of the array.
        """
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()