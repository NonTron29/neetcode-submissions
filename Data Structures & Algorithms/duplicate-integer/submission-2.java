class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap <Integer, Integer> map = new HashMap<>();
        int count = 0;
        for (int i = 0; i < nums.length; i++) {
            int compare = nums[i];
            if (map.containsKey(compare)){
                count++;
            }
            else {
                map.put(nums[i],i);
            }
        }
        return count != 0;
    }
}