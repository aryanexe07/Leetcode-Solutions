class Solution:
    def countKdivPairs(self, arr, k):
        freq = {}
        ans = 0

        for num in arr:
            rem = num % k
            need = (k - rem) % k

            ans += freq.get(need, 0)
            freq[rem] = freq.get(rem, 0) + 1

        return ans
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna