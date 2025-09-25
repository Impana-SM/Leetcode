class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        revNum = 0
        sign = -1 if x < 0 else 1  
        x = abs(x)
        while x > 0:
             ld = x % 10
             revNum = (revNum * 10) + ld
             x = x // 10
        revNum *= sign  
        if revNum < -2**31 or revNum > 2**31 - 1:
            return 0
        return revNum
     
        
       

        