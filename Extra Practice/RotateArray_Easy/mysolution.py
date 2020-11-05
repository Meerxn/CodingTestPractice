import copy
def rotate( nums, k: int) -> None:
    temp = []
    temp = [0] * k 
    x = nums.copy()
    index = len(nums) -1 
    numsI = 0
    for i in range(len(temp) - 1 , -1 , -1 ):
        temp[i] = nums[index]
        index  = index - 1
    j = 0 
    for i in range(0,len(nums)):
        if i < k:
            nums[i] = temp[i]
        else:

             nums[i] = x[j]
             j = j +1
        
        

    print(nums[:])
rotate([1,2,3,4,5,6,7] , 3)           

