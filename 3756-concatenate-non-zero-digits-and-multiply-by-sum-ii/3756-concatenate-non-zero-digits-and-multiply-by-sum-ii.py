class Solution(object):
    def sumAndMultiply(self, s, queries):
        MOD = 10**9 + 7
        n = len(s)

        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        cnt = [0] * (n + 1)
        sumPref = [0] * (n + 1)
        prefVal = [0] * (n + 1)

        for i, ch in enumerate(s):
            d = ord(ch) - ord('0')
            cnt[i + 1] = cnt[i]
            sumPref[i + 1] = sumPref[i]

            if d != 0:
                cnt[i + 1] += 1
                sumPref[i + 1] += d
                prefVal[i + 1] = (prefVal[i] * 10 + d) % MOD
            else:
                prefVal[i + 1] = prefVal[i]

        ans = []

        for l, r in queries:
            k = cnt[r + 1] - cnt[l]

            x = (prefVal[r + 1] - prefVal[l] * pow10[k]) % MOD
            digitSum = sumPref[r + 1] - sumPref[l]

            ans.append((x * digitSum) % MOD)

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna