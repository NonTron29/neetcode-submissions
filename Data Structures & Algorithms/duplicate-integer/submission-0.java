class Solution {
    public boolean hasDuplicate(int[] nums) {
    Map <Integer, Integer> numMap = new HashMap<>();
    int count = 0;
    for (int i = 0; i < nums.length; i++) {
        int compare = nums[i];
        if (numMap.containsKey(compare)) {
            count++;
        }
        numMap.put(nums[i],i);

    }
    return count != 0;    
    }
}