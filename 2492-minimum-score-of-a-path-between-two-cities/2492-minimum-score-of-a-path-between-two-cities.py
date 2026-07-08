class Solution(object):
    def minScore(self, n, roads):
        from collections import defaultdict, deque

        graph = defaultdict(list)
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        q = deque([1])
        visited = {1}
        ans = float('inf')

        while q:
            node = q.popleft()

            for nei, wt in graph[node]:
                ans = min(ans, wt)
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna