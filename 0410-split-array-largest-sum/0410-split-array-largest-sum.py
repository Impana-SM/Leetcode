class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def can_split(mid):
            count = 1
            curr_sum = 0
            for num in nums:
                curr_sum += num
                if curr_sum > mid:
                    count += 1
                    curr_sum = num
            return count <= k

        low, high = max(nums), sum(nums)
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if can_split(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
        