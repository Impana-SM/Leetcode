class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        # number of even positions (ceil(n/2))
        even_count = (n + 1) // 2
        # number of odd positions (floor(n/2))
        odd_count = n // 2

        # Compute (5^even_count * 4^odd_count) % MOD
        result = (pow(5, even_count, MOD) * pow(4, odd_count, MOD)) % MOD
        return result
        