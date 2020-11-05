
    
def removeDuplicates(self, nums: List[int]) -> int:
    nD = []
    j = 1 
    
    for i in range (1,len(nums)):
        if nums[j-1] == nums[i]:
            continue
        else:
            nums[j] = nums[i]
            j +=1
    
    return j


removeDuplicates([1,1,2]) 