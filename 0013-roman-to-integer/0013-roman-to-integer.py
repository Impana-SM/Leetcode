class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        
        res = 0
        
        # Loop through the string, except the last character
        for i in range(len(s) - 1):
            # Subtract if current value is less than next
            if roman[s[i]] < roman[s[i + 1]]:
                res -= roman[s[i]]
            else:
                # Otherwise, add the value
                res += roman[s[i]]
        
        # Add the value of the last character
        return res + roman[s[-1]]
        