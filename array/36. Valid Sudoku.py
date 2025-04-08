from typing import List;

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # i can use hashset to check for duplicates for row and col 
        for r in range(9):
            hashset = set()
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in hashset:
                    return False
                else:
                    hashset.add(board[r][c])
        for c in range(9):
            hashset = set()
            for r in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in hashset:
                    return False
                else:
                    hashset.add(board[r][c])
        for square in range(9):
            hashset = set()
            for r in range(3):
                for c in range(3):
                    row = (square//3)*3 + r
                    col = (square%3)*3 + c
                    if board[row][col] == '.':
                        continue
                    if board[row][col] in hashset:
                        return False
                    else:
                        hashset.add(board[row][col])
        return True
