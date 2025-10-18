class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        left = 0
        right = len(s) - 1

        # Trim leading and trailing spaces
        while left <= right and s[left] == ' ':
            left += 1
        while right >= left and s[right] == ' ':
            right -= 1

        temp = ""
        ans = ""

        while left <= right:
            ch = s[left]

            if ch != ' ':
                temp += ch
            else:
                # if current char is space and temp is not empty, add word to result
                if temp != "":
                    if ans != "":
                        ans = temp + " " + ans
                    else:
                        ans = temp
                    temp = ""
            left += 1

        # Add the last word
        if temp != "":
            if ans != "":
                ans = temp + " " + ans
            else:
                ans = temp

        return ans
        