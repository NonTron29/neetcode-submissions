class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int d = 0;
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < numbers.length; i++) {
            d = target - numbers[i];
            if (map.containsKey(d)) {
                return new int[] {map.get(d) + 1,i + 1};
            }
            else {
                map.put(numbers[i], i);
            }
        }
        return new int[] {};
    }
}
