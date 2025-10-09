class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            # Found target
            if nums[mid] == target:
                return mid

            # Check which half is sorted
            if nums[low] <= nums[mid]:  # Left half sorted
                if nums[low] <= target < nums[mid]:
                    high = mid - 1  # Search left
                else:
                    low = mid + 1   # Search right
            else:  # Right half sorted
                if nums[mid] < target <= nums[high]:
                    low = mid + 1   # Search right
                else:
                    high = mid - 1  # Search left
        
        return -1  # Not found