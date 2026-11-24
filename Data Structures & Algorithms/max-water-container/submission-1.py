class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        t = 0
        maxed = 0

        while (l < r):
            m = min(heights[l], heights[r])
            t = (r - l) * m
            maxed = max(t, maxed)
            if (heights[l] < heights[r]):
                l += 1
            else:
                r -= 1
            

        return maxed