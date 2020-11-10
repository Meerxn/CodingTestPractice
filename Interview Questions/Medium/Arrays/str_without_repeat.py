import math
'''
This solution is by @nedLarsen435 on leetcode. This uses the sliding window concept along with a set checking for repeats 
during ietration. Each time we find a duplicate we pop from the start of our set until we find our duplicate 
and then we continue from there. i is the right index l is the left index. we take the distance between the l and r after adding something as the 
curr max but we make sure to check for the duplicates before we add to stop the code from counting the duplicate itself
'''
def lengthOfLongestSubstring(s):
    curr = set()
    ans = []
    mx = -math.inf
    left = 0 
    if s == "":
        return 0
    l = 0 
    for i in range(len(s)):
        while s[i] in curr:
            curr.remove(s[l])
            
            l+=1
        curr.add(s[i])
        left = max(i-l+1 , left)
        
    return left
s = "abcabcbb"
print(lengthOfLongestSubstring(s))

