class Solution {
    public boolean isHappy(int n) {
        Set<Integer> map = new HashSet<> ();
        while (!map.contains(n)) {
            map.add(n);
            n = happy(n);
            if (n == 1){
                return true;
            }
        }
        return false;
    }

    public int happy(int n) {
        int sum = 0;
        while (n > 0) {
            sum += ((n % 10) * (n % 10));
            n /= 10;
        }
        return sum;
    }
}
