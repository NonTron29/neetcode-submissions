class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        n = len(board)
        m = len(board[0])

        for r in range(n):
            for c in range(m):
                if board[r][c] == '.':
                    continue
                if board[r][c] in row[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3, c//3)]:
                    return False
                else:
                    row[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    squares[(r // 3, c// 3)].add(board[r][c])
                    
            
        return True

        
        
        