class Solution(object):
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        if (m + n - 1) % 2 == 1:
            return False

        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        memo = {}

        def dfs(i, j, balance):

            if grid[i][j] == '(':
                balance += 1
            else:
                balance -= 1

            if balance < 0:
                return False

            remaining = (m - 1 - i) + (n - 1 - j)

            if balance > remaining:
                return False

            if i == m - 1 and j == n - 1:
                return balance == 0

            key = (i, j, balance)

            if key in memo:
                return memo[key]

            if i + 1 < m:
                if dfs(i + 1, j, balance):
                    memo[key] = True
                    return True

            if j + 1 < n:
                if dfs(i, j + 1, balance):
                    memo[key] = True
                    return True

            memo[key] = False
            return False

        return dfs(0, 0, 0)