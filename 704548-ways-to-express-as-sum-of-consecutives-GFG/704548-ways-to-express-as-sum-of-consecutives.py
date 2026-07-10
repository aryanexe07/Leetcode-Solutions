class Solution:
    def getCount(self, n):
        count = 0
        k = 2

        while k * (k + 1) // 2 <= n:
            num = n - k * (k - 1) // 2
            if num > 0 and num % k == 0:
                count += 1
            k += 1

        return count
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna