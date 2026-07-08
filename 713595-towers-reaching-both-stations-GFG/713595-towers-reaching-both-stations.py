from collections import deque

class Solution:
    def countCoordinates(self, mat):
        n, m = len(mat), len(mat[0])

        def bfs(starts):
            vis = [[False] * m for _ in range(n)]
            q = deque()

            for r, c in starts:
                if not vis[r][c]:
                    vis[r][c] = True
                    q.append((r, c))

            dirs = [(1,0), (-1,0), (0,1), (0,-1)]

            while q:
                r, c = q.popleft()

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < n and 0 <= nc < m and
                        not vis[nr][nc] and
                        mat[nr][nc] >= mat[r][c]):
                        vis[nr][nc] = True
                        q.append((nr, nc))

            return vis

        # Station P: top row + left column
        p = [(0, j) for j in range(m)] + [(i, 0) for i in range(n)]

        # Station Q: bottom row + right column
        q = [(n - 1, j) for j in range(m)] + [(i, m - 1) for i in range(n)]

        visP = bfs(p)
        visQ = bfs(q)

        ans = 0
        for i in range(n):
            for j in range(m):
                if visP[i][j] and visQ[i][j]:
                    ans += 1

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna