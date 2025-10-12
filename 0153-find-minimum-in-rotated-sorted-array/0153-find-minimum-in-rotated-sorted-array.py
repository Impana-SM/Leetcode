class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        ans = sys.maxsize
        while low <= high:
             mid = (low + high) // 2

        # search space is already sorted
        # then arr[low] will always be
        # the minimum in that search space:
             if nums[low] <= nums[high]:
                     ans = min(ans, nums[low])
                     break
            
             if nums[low] <= nums[mid]:  # if left part is sorted
                      ans = min(ans, nums[low])  # keep the minimum
                      low = mid + 1  # eliminate left half

             else:  # if right part is sorted
                     ans = min(ans, nums[mid])  # keep the minimum
                     high = mid - 1  # eliminate right half

        return ans
        