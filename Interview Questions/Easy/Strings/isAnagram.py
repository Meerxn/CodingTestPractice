class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = {}
        dic2 = {}
        for i in s:
            try:
                dic1[i]+=1
            except:
                dic1[i] = 1
                continue
        for j in t:
            try:
                dic2[j]+=1
            except:
                dic2[j] = 1 
                continue
        return dic1 == dic2
        