class Solution(object):
    def sumAndMultiply(self, n):
        x = 0
        digit_sum = 0

        for ch in str(n):
            if ch != '0':
                d = int(ch)
                x = x * 10 + d
                digit_sum += d

        return x * digit_sum

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna