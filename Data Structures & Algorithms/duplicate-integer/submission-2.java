class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> had = new HashSet<>();
        for (int num : nums) {
            if (had.contains(num)) {
                return true;
            }
            had.add(num);
        }
        return false;
    }
}