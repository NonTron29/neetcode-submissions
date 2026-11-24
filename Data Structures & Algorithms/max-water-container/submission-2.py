class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxed = 0

        while (l < r):
            t = (r - l) * min(heights[l], heights[r])
            maxed = max(t, maxed)
            if (heights[l] < heights[r]):
                l += 1
            else:
                r -= 1
            
        return maxed