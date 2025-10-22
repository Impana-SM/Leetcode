class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) != len(goal):
            return False  
        doubled_s = s + s  # Concatenate s with itself
        return goal in doubled_s 
        