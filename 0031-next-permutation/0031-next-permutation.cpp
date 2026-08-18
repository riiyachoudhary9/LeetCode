class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int n = nums.size();
        
        // 1. Find the first element from the right
        //    that is smaller than the element after it.
        int i = n - 2;
        while (i >= 0 && nums[i] >= nums[i + 1]) {
            i--;
        }

        // 2. Find the smallest element greater than nums[i]
        //    from the right and swap.
        if (i >= 0) {
            int j = n - 1;
            while (nums[j] <= nums[i]) {
                j--;
            }
            swap(nums[i], nums[j]);
        }

        // 3. Reverse the suffix to get the smallest
        //    possible arrangement.
        reverse(nums.begin() + i + 1, nums.end());
    }
};