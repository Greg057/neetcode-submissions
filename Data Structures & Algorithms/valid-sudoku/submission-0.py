class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = {}
        rows = {}
        squares = {}

        for i in range(9):
            cols[i] = set()
            rows[i] = set()
        
        for j in range(3):
            for k in range(3):
                squares[(j, k)] = set()

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rows[r] or 
                   board[r][c] in cols[c] or
                   board[r][c] in squares[(r//3, c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True       

        