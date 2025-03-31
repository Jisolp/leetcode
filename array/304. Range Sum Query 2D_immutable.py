from typing import List;

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        #initalize a new matrix that has the sum with the left and the upper padded w 0 
        row, col = len(matrix), len(matrix[0])
        self.sumMatrix = [[0]*(col+1) for r in range(row+1)]

        for r in range(row):
            prefix = 0
            for c in range(col):
                prefix += matrix[r][c]
                prev = self.sumMatrix[r][c+1]
                self.sumMatrix[r+1][c+1] = prefix + prev

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        aboveSum = self.sumMatrix[row1][col2+1]
        leftSum = self.sumMatrix[row2+1][col1]
        leftCorner = self.sumMatrix[row1][col1]
        ans = self.sumMatrix[row2+1][col2+1] - aboveSum - leftSum + leftCorner
        return ans