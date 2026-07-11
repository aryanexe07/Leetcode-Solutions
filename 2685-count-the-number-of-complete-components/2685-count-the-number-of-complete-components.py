class Solution(object):
    def countCompleteComponents(self, n, edges):
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        ans = 0

        def dfs(node, comp):
            visited[node] = True
            comp.append(node)

            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei, comp)

        for i in range(n):
            if not visited[i]:
                comp = []
                dfs(i, comp)

                nodes = len(comp)
                edge_count = 0

                for node in comp:
                    edge_count += len(graph[node])

                edge_count //= 2

                if edge_count == nodes * (nodes - 1) // 2:
                    ans += 1

        return ans
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna