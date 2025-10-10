class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        n = len(nums)  
        low, high = 0, n - 1
        while low <= high:
             mid = (low + high) // 2
        # if mid points to the target
             if nums[mid] == target:
                 return True
        # Edge case:
             if nums[low] == nums[mid] and nums[mid] == nums[high]:
                  low += 1
                  high -= 1
                  continue
        # if left part is sorted
             if nums[low] <= nums[mid]:
                 if nums[low] <= target <= nums[mid]:
                      high = mid - 1
                 else:
                      low = mid + 1
             else:  # if right part is sorted
                 if nums[mid] <= target <= nums[high]:
                       low = mid + 1
                 else:
                       high = mid - 1

        return False
        