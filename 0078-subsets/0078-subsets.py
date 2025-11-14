class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def backtrack(start, path):
            # Add the current subset to the result
            res.append(path[:])
            # Explore further elements
            for i in range(start, len(nums)):
                # Include nums[i] and move forward
                path.append(nums[i])
                backtrack(i + 1, path)
                # Backtrack
                path.pop()

        backtrack(0, [])
        return res

        