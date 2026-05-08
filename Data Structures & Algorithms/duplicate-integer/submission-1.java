class Solution {
    public boolean hasDuplicate(int[] nums) {
        for (int i = 0; i <= nums.length - 1; i++) {
            for (int j = 1; j <= nums.length - 1; j++)
                if (nums[i] == nums[j] && i!=j)
                    return true;
        }
        return false;
    }
}