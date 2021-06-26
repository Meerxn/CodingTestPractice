class Solution:
    def reverse(self, x: int) -> int:
        
        y = str(abs(x))
        print(y)
        if x < 0:
            val = int( "-" + y[::-1])
            return val if val <= 2**31 -1 and val >= -2**31 else 0
        else:
            val = int(y[::-1])
            return val if val <= 2**31 -1 and val >= -2**31 else 0
            