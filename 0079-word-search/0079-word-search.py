class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        
        self.rows = len(board)
        self.cols = len(board[0])
        self.word = word
        
        def dfs(r, c, idx):
            # If all letters are found
            if idx == len(word):
                return True
            
            # Check boundaries and current character match
            if r < 0 or r >= self.rows or c < 0 or c >= self.cols or board[r][c] != word[idx]:
                return False
            
            # Mark the cell as visited by temporarily changing its value
            temp = board[r][c]
            board[r][c] = "#"
            
            # Explore all 4 directions: up, down, left, right
            found = (dfs(r+1, c, idx+1) or
                     dfs(r-1, c, idx+1) or
                     dfs(r, c+1, idx+1) or
                     dfs(r, c-1, idx+1))
            
            # Restore the cell's original value
            board[r][c] = temp
            
            return found
        
        # Start DFS from each cell
        for i in range(self.rows):
            for j in range(self.cols):
                if dfs(i, j, 0):
                    return True
        
        return False