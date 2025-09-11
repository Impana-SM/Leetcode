class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        cnt = 0  # Count
        el = None  # Element

   
        for i in range(n):
             if cnt == 0:
                 cnt = 1
                 el = nums[i]
             elif el == nums[i]:
                 cnt += 1
             else:
                 cnt -= 1

    
        cnt1 = 0
        for i in range(n):
             if nums[i] == el:
                 cnt1 += 1

        if cnt1 > (n / 2):
             return el
        return -1