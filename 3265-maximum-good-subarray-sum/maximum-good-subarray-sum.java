
import java.util.*;

class Solution {
    public long maximumSubarraySum(int[] nums, int k) {

        HashMap<Long, Long> map = new HashMap<>();

        long prefixSum = 0;
        long ans = Long.MIN_VALUE;

        for (int num : nums) {

            // Check both possible starting values
            long a = (long) num - k;
            long b = (long) num + k;

            // Find maximum good subarray sum
            if (map.containsKey(a)) {
                ans = Math.max(ans, prefixSum + num - map.get(a));
            }

            if (map.containsKey(b)) {
                ans = Math.max(ans, prefixSum + num - map.get(b));
            }

            // Store minimum prefix sum for this number
            map.put((long) num,
                Math.min(map.getOrDefault((long) num, Long.MAX_VALUE),
                         prefixSum));

            // Update prefix sum
            prefixSum += num;
        }

        return ans == Long.MIN_VALUE ? 0 : ans;
    }
}
