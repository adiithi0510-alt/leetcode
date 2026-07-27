class Solution {
    public int maxProduct(int[] nums) {
       Arrays.sort(nums);
       int First=nums[nums.length-1];
       int Second=nums[nums.length-2];
       int result=(First-1)*(Second-1);
       return result; 
    }
}