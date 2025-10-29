class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start, end = 0, 0

        # Iterate through each character as center
        for center in range(len(s)):
            # Expand around odd length
            len1 = self.expandFromCenter(s, center, center)
            # Expand around even length
            len2 = self.expandFromCenter(s, center, center + 1)
            # Maximum length from both cases
            max_len = max(len1, len2)

            # Update the boundaries if longer palindrome found
            if max_len > end - start:
                start = center - (max_len - 1) // 2
                end = center + max_len // 2

        # Return the longest palindromic substring
        return s[start:end + 1]

    def expandFromCenter(self, s, left, right):
        # Expand while valid and characters match
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return the length of the palindrome
        return right - left - 1
        