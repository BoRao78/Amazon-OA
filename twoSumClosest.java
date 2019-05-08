public class Solution {
    /**
     * @param nums an integer array
     * @param target an integer
     * @return the difference between the sum and the target
     */
    public int twoSumClosest(int[] nums, int target) {
        // Write your code here
        
        Arrays.sort(nums);
        
        int min = target;
        
        int left = 0;
        int right = nums.length - 1;
        int largest = 0;
        int[] res = {};

        while (left < right) {
            if (nums[left] + nums[right] < target) {
                min = Math.min(min, target - nums[left] - nums[right]);
                left++;
            }
            else {
                min = Math.min(min, nums[left] + nums[right] - target);
                right--;
            }
        }
        
        return min;
    }

    public int main() {

        int [] movie_duration = {90, 85, 75, 60, 120, 150, 125};
        int d = 250;
        this.twoSumClosest(movie_duration, d);
    }
}