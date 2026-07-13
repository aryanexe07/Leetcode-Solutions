from math import gcd

class Solution:
    def minOperations(self, b):
        MOD = 10**9 + 7
        n = len(b)

        visited = [False] * n
        lcm = 1

        for i in range(n):
            if not visited[i]:
                curr = i
                length = 0

                while not visited[curr]:
                    visited[curr] = True
                    curr = b[curr] - 1   # convert to 0-based indexing
                    length += 1

                lcm = lcm * length // gcd(lcm, length)

        return lcm % MOD

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna