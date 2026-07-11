class Solution:
    def longestPath(self, mat, xs, ys, xd, yd):
        n = len(mat)
        m = len(mat[0])

        if mat[xs][ys] == 0 or mat[xd][yd] == 0:
            return -1

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(x, y):
            if x == xd and y == yd:
                return 0

            mat[x][y] = 0      # mark visited
            ans = -1

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < m and mat[nx][ny] == 1:
                    cur = dfs(nx, ny)
                    if cur != -1:
                        ans = max(ans, cur + 1)

            mat[x][y] = 1      # backtrack
            return ans

        return dfs(xs, ys)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna