class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        return self.atMost(nums, goal) - self.atMost(nums, goal - 1)

    # Helper function to compute subarrays with sum at most k
    def atMost(self, nums, k):
        # No subarrays for negative sum
        if k < 0:
            return 0

        left = 0
        total = 0
        curr_sum = 0

        # Traverse array using right pointer
        for right in range(len(nums)):
            # Add current element to sum
            curr_sum += nums[right]

            # Shrink window if sum exceeds k
            while curr_sum > k:
                curr_sum -= nums[left]
                left += 1

            # Add number of valid subarrays ending at right
            total += (right - left + 1)

        return total
        