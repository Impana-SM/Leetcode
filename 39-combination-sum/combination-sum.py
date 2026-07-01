class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, current, remaining):
            # target reached
            if remaining == 0:
                result.append(current.copy())
                return

            # try all candidates from start index
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    continue

                current.append(candidates[i])

                # same i because we can reuse the same number
                backtrack(i, current, remaining - candidates[i])

                current.pop()

        backtrack(0, [], target)

        return result
            