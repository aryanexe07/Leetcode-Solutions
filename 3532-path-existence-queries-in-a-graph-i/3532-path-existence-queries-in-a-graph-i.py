class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        comp = [0] * n
        cid = 0

        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                cid += 1
            comp[i] = cid

        return [comp[u] == comp[v] for u, v in queries]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna