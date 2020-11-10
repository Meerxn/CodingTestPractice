'''
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Notes: this algo takes longer due to the keys check to see first element or not this can
be avoided by using collectiions.default dict and directly appending to that. 

The main idea of this solution is that each anagram will have the same sorted set of alphabets and those can 
be used as keys for dictionary with value types as list. 


'''

def groupAnagrams(strs):
    # Use this and directly append to avoid the if check
    #f = collections.defaultdict(list)
    ans = []
    x = len(strs)
    if x == 0:
        return [[""]]
    if x == 1:
        return[strs]
    dict = {}          
    for i in range (x):
        if tuple(sorted(strs[i])) not in dict.keys():
            dict[tuple(sorted(strs[i]))] = [strs[i]]
        else:
            dict[tuple(sorted(strs[i]))].append(strs[i])     
    
    
    return dict.values()       
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
