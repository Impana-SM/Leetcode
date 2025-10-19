class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        ind = -1
        
        # Iterate through the string from the end to beginning
        i = 0
        for i in range(len(num) - 1, -1, -1):
            # Break if an odd digit is found
            if (int(num[i]) % 2) == 1:
                ind = i
                break
        
        # Skipping any leading zeroes
        i = 0
        while i <= ind and num[i] == '0':
            i += 1
        
        # Return the largest odd number substring
        return num[i:ind + 1]
 
        