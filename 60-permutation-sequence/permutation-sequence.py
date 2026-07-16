class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = []
        for i in range(1, n + 1):
            numbers.append(str(i))
        factorial = [1] * n
        for i in range(1, n):
            factorial[i] = factorial[i - 1] * i
        k -= 1
        result = ""
        for i in range(n, 0, -1):
            index = k // factorial[i - 1]
            result += numbers[index]
            numbers.pop(index)
            k = k % factorial[i - 1]

        return result
        