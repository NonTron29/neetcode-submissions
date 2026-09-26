class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int l = 0;
        int r = numbers.length - 1;
        int sum = 0;
        while (r > l) {
            sum = numbers[l] + numbers[r];
            if (sum > target) r--;
            if (sum < target) l++;
            if (sum == target) return new int[] {l+1, r+1};
        }
        return new int[0];
    }
}
