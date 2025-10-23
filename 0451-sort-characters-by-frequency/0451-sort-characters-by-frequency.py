class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # Step 2: Sort by frequency (descending), then by character
        sorted_chars = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

        # Step 3: Build the result string by repeating characters
        result = ''.join([ch * count for ch, count in sorted_chars])

        return result