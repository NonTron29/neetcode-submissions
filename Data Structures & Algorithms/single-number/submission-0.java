class Solution {
    public int singleNumber(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            int count = 0;
            for (int j = 0; j < nums.length; j++) {
                if (j != i && nums[j] == nums[i]) {
                    count++;
                }
            }
            if (count == 0) {
                return nums[i];
            }
        }
        return -1;
    }
}
