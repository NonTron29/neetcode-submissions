class Solution {
    public int maxArea(int[] heights) {
        int total = 0;
        int l = 0;
        int r = heights.length - 1;
        int max = 0;

        while (r > l) {
           int min = min(heights[l], heights[r]);
           total = (r - l) * min;
            if (total > max) max = total;
            if (heights[l] > heights[r]) {
                r--;
            }
            else {
                l++;
            }

        }

        return max;
        
    }

    public int min(int l, int r) {
        if (l > r) return r;
        if (r > l) return l;
        if (r == l) return r;

        return 0;
    }
}
