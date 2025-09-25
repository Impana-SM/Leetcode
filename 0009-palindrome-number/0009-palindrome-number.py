class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        revNum = 0
        dup = x
        while x > 0:
             ld = x % 10
             revNum = (revNum * 10) + ld
             x = x // 10
        if dup == revNum:
             return True
        else:
             return False
        
        