
def longestPalindrome(s):
    ## MY SOLUTION 
    '''
    n = len(s)
    longest = ""
    if n == 1:
        return s
    if n == 2:
        if s[0] == s[1]:
            return s
        else:
            return s[0]    
    mainL = s[0]
    l = 0 
    r = 0
    even = False
    
    for i in range(n):
        
            if i == 0 or i == n -1:
                continue
            centre = s[i]
            if n % 2 == 1: 
                l = i 
                r = i 
            elif n %2 ==0:
                even = True
                l = i
                r = i+1


            count = 0 
            while s[l] == s[r]:
                if count == 0 and even == True:
                    longest = s[l] + s[r] 
                    count += 1
                elif count == 0 and even == False:
                    longest = centre  
                    count += 1
                else:
                    longest = s[l] + longest + s[r]
                    count += 1
                l -=1
                r +=1
                
                if l < 0 or r == n:
                   
            
                    break 
            print(longest,mainL)

            if len(longest) > len(mainL):
                mainL = longest
    return mainL
    '''
    n = len(s)
    longest = ""
    if n == 1:
        return s
    if n == 2:
        if s[0] == s[1]:
            return s
        else:
            return s[0]
    if n %2 == 0:
        


print(longestPalindrome("abb"))


            



        