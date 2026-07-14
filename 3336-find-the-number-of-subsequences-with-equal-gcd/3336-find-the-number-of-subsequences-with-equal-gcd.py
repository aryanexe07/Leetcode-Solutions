class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def subsequencePairCount(self, nums):
        MOD = 10**9 + 7

        dp = {(0, 0): 1}

        for x in nums:
            ndp = {}

            for (g1, g2), cnt in dp.items():
                # Ignore
                ndp[(g1, g2)] = (ndp.get((g1, g2), 0) + cnt) % MOD

                # Put in seq1
                ng1 = x if g1 == 0 else self.gcd(g1, x)
                ndp[(ng1, g2)] = (ndp.get((ng1, g2), 0) + cnt) % MOD

                # Put in seq2
                ng2 = x if g2 == 0 else self.gcd(g2, x)
                ndp[(g1, ng2)] = (ndp.get((g1, ng2), 0) + cnt) % MOD

            dp = ndp

        ans = 0
        for (g1, g2), cnt in dp.items():
            if g1 != 0 and g1 == g2:
                ans = (ans + cnt) % MOD

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna