def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        a = [0] * n
        for i in range(n):
            # Learn the modulo formula and how it works \
            a[(i + k) % n] = nums[i]
            
        # nums copy    
        nums[:] = a