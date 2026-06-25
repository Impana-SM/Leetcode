class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        used = [False] * len(nums)

        def backtrack(path):
            
            # permutation completed
            if len(path) == len(nums):
                result.append(path.copy())
                return
            
            for i in range(len(nums)):
                
                # already used element
                if used[i]:
                    continue
                
                # skip duplicates
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                
                # choose
                used[i] = True
                path.append(nums[i])

                backtrack(path)

                # undo choice
                path.pop()
                used[i] = False


        backtrack([])

        return result
        