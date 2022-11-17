"""
https://www.youtube.com/watch?v=Ph95IHmRp5M
"""

def solveNQueens(n):
    col = set()
    posDiag = set() # (r + c)
    negDiag = set() # (r - c)
    res = []
    board = [["."] * n for _ in range(n)]
    def backtrack(r):
        if r == n:
            res.append(["".join(row) for row in board])
            return
            
        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue
            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "Q"

            backtrack(r + 1)

            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "."
    backtrack(0)
    return res

print(solveNQueens(4))