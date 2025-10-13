class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        left, right = 1, max(nums)
        
        # Helper function to compute sum with a given divisor
        def compute_sum(divisor):
            return sum(math.ceil(num / float(divisor)) for num in nums)
        
        # Binary search to find smallest divisor
        while left < right:
            mid = (left + right) // 2
            if compute_sum(mid) > threshold:
                # divisor too small → increase it
                left = mid + 1
            else:
                # divisor works → try smaller one
                right = mid
                
        return left