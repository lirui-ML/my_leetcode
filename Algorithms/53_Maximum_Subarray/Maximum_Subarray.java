/*
描述：最大子序和，难度（easy）
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/

class Solution {
    public int maxSubArray(int[] nums) {
    	//动态规划
    	if (nums == null || nums.length == 0)
    		return 0;
    	int n = nums.length;
    	int[] dp = new int[n];
    	dp[0] = nums[0];
    	int result = dp[0];
    	for (int i = 1;i < n;i++) {
    		dp[i] = Math.max(dp[i - 1] + nums[i], nums[i]);
    		result = Math.max(result, dp[i]);
    	}
    	return result;
    }
    
    public int maxSubArray_2(int[] nums) {
    	//动态规划2
    	int n = nums.length;
    	int maxSum = nums[0];
    	for (int i = 1; i < n; i++) {
    		if (nums[i - 1] > 0) {
    			nums[i] += nums[i - 1];
			}
    		maxSum = Math.max(nums[i], maxSum);
		}
    	return maxSum;
    }
}