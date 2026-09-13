class Solution(object):
    def luckyNumbers(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        result = []
        for i in range(rows):
            minimum = min(matrix[i])
            for j in range(cols):
                if matrix[i][j] == minimum:
                    column = [matrix[k][j] for k in range(rows)]
                    if minimum == max(column):
                        result.append(minimum)
        return result