class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binarySearch(nums, target, findFirst):
            low, high = 0, len(nums) - 1
            ans = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    ans = mid
                    if findFirst:
                        high = mid - 1  # go left
                    else:
                        low = mid + 1   # go right
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return ans

        first = binarySearch(nums, target, True)
        last = binarySearch(nums, target, False)
        return [first, last]