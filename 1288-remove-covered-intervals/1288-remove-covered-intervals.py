class Solution(object):
    def removeCoveredIntervals(self, intervals):
        intervals.sort(key=lambda x: (x[0], -x[1]))

        ans = 0
        max_end = 0

        for start, end in intervals:
            if end > max_end:
                ans += 1
                max_end = end

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna