
   
def subsets( nums):
    ans = []
    if len(nums) == 0 :
        return []
    
    backt(0,ans,[],nums)
    return ans

def backt(start,ans,curr,nums):
    if(len(curr) > len(nums)):
        return
    
    ans.append(list(curr))
    print(start,curr)
    
    for i in range(start,len(nums)):

        curr.append(nums[i])
        print(i,i+1,nums[i])
        backt(i+1,ans,curr,nums)
        (curr.pop(len(curr)-1))
        


print(subsets([1,2,3]))




        