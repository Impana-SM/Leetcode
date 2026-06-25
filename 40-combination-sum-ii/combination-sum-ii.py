class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtrack(start, path, remaining):
            
            if remaining == 0:
                result.append(path.copy())
                return
            
            for i in range(start, len(candidates)):
                
                # Skip duplicate numbers at same level
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                # No need to continue if number is greater than remaining sum
                if candidates[i] > remaining:
                    break
                
                path.append(candidates[i])

                # Move i+1 because each number can be used only once
                backtrack(i + 1, path, remaining - candidates[i])

                path.pop()

        backtrack(0, [], target)

        return result
        