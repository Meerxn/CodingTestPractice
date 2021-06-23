
import math
def waitingTime(tickets,p):
    timeCount = 0
    alex = tickets[p]
    while tickets[p] != 0:
        for i in range(len(tickets)):
            tickets[i] = tickets[i] -1
            if tickets[p] == 0 :
                break
            timeCount +=1
            
    return timeCount



print (waitingTime([2,6,3,4,5] , 2))



def autoscale(utils,instances):
    index = 0 
    while index < len(utils) :
        print(utils[index] , instances)
        if utils[index] >= 25 and  utils[index]<= 60:
            index = index + 1
            continue
        elif utils[index] < 25:
            if instances > 1:
                instances = instances/2
            
                index = index + 10
            else:
                index +=1
                continue
            
        elif utils[index] >60:
            instances = instances * 2
            index = index + 10

        
    print(instances)
arr = [5,10,80]
instance = 1
autoscale(arr,1)



#Twitter Question 1 
def buyingShowTickets(arr,p):
    count = 0 
    while arr[p] != 0:
        
        
        for i in range(len(arr)):
            arr[i] = arr[i] - 1
            
            if [arr[p]] == 0:
                
                break
            count +=1
    return count
print("Buying showing tickets")
print(waitingTime([2,6,3,4,5] , 2))


'''
def subplaindrome(s):


    #Odd strings
    u = len(s)/2
    u = math.floor(u)
    left = u - 1 
    right
    return u

    


#aakkaa
print(subplaindrome("aakkaa"))
'''
#tacocat
'''
def twitterSoc(related)
    groupDict = {}
'''


def iterate(s, left, right, str):

    # run till str[low.high] is a palindrome
    while left >= 0 and right < len(str) :
        if str[left] == str[right]: 
    
    

            # push all palindromes into the set
            s.add(str[left: right + 1])

            # expand in both directions
            left -= 1
            right += 1
        else:
            break
def subp(s):
    stringSet = set()
    sType = ""
    
    #Ideas


    # Use a set since we checking unique vals
    # Main goal is to center every indexed string and expand out
    # like a sliding window that expands both ways ?
    #  what if repeated matches

    # We need to account for the checks by using lengths as a check

    #check for type length of string and do calls


    #Odd length example:
    # Racecar -- take e as center and scale up/down
    #Doubt how do we deal when the substrings are even ?
    # alternate lengths via scaling differently
    for x in range(len(s)):

        left = x 
        right = x + 1 
        #even scaling would use 
        #akka -- becomes a k low high then k k which goes to a k k a so 
        #this  method works for even
        iterate(stringSet,left,right,s)

        #one center 
        left = x 
        right = x



        #racecar scale
        iterate(stringSet,low,high,s)

    return stringSet
print(subp("google"))    


def numberOfProvinces(isConnected):

    def dfs(curr):
        visited.add(curr):
        for neighbour in range(len(isConnected)):
            if neighbour not in visited and isConnected[curr][neighbour] ==1:
                dfs(neighbour)


    groups = 0
    visited = set()
    for curr in range(len(isConnected)):
        if curr not in visited:
            groups +=1
            dfs(curr)



class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        def dfs(curr):
            visited.add(curr)
            for neighbour in range(len(isConnected)):
                if neighbour not in visited and isConnected[curr][neighbour] ==1:
                    dfs(neighbour)


        groups = 0
        visited = set()
        for curr in range(len(isConnected)):
            if curr not in visited:
                groups +=1
                dfs(curr)
        return groups

public static int balancedSum(List<Integer> sales) {
    // Write your code here     
		sum =0;
        for i in range(len((int i=0;i<list.size();i++){
            sum += list.get(i);
        }
        int curr =list.get(0);
        for(int i=1;i<list.size();i++){
            if(curr == sum - curr - list.get(i)){
                return i;
            }
            curr += list.get(i);
        }
        return -1;
    }





    #!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'balancedSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY sales as parameter.
#

def balancedSum(sales):
    # Write your code here
    sumVal = 0
    for i in range(len(sales)):
        sum += sales[i]
    current = sales[0]
    for i in range(1,len(sales)):
        if current == sum - current  - sales[i]:
            return i
        current += sales[i]

if __name__ == '__main__':



    #!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'restock' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY itemCount
#  2. INTEGER target
#

def restock(itemCount, target):
    # Write your code here
    total = 0
    for i in range(len(itemCount)):
        
        total += itemCount[i]
        if total > target:
            return total - target
        elif i == len(itemCount ) - 1 and total < target:
            return target - total
            
        
    
    pass
if __name__ == '__main__':




    #!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getMinimumDifference' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY a
#  2. STRING_ARRAY b
#
import collections
def getMinimumDifference(a, b):
    arr = []
    def helper(a,b):
        if len(a) == len(b):
            
            cA = collections.Counter(a)
            cB  = collections.Counter(b)
            diff = cA - cB
            ans = sum(diff.values())
            return ans
        else:
            return -1
    for i in range(len(a)):
        arr.append(helper(a[i],b[i]))
    return arr
    # Write your code here
    
    #Try using collections.counter()
    
    
if __name__ == '__main__':




    #!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'carParkingRoof' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY cars
#  2. INTEGER k
#
import math
import sys
def carParkingRoof(cars, k):
    #kcars
    #k chose algo
    rangeVal = len(cars) - k + 1
    cars = sorted(cars)
    count = 0
    mx = sys.maxsize
    res = mx
    while count < rangeVal:
        cover = count + k 
        diff = cars[cover - 1] - cars[count]
        diff+=1
        res = min(mx,res,diff)
        count +=1
    return res
        
        
        
    
    print(cars)

if __name__ == '__main__':  
