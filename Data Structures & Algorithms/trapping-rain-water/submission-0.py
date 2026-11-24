class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0 
        r = len(height) - 1
        area = 0

        lm = 0
        rm = 0

        while l < r:
            if height[l] <= height[r]:
                lm = max(lm, height[l])
                area += lm - height[l]
                l += 1

            else:
                rm = max(rm, height[r])
                area += rm - height[r]
                r -= 1

            

        return area

            

        