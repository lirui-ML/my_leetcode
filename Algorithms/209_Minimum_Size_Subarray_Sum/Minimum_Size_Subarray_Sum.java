/*
描述： 长度最小的子数组（难度：medium）
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。

示例:

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
进阶:

如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
 */

class Solution {
  public int minSubArrayLen(int s, int[] nums) {
    //滑动窗口，时间复杂度
    if (nums == null || nums.length == 0) {
      return 0;
    }
    int i = 0, j = 0, sum = 0, min = Integer.MAX_VALUE;
    while (j < nums.length) {
      sum += nums[j++];
      while (sum >= s) {
        min = Math.min(min, j - i);
        sum -= nums[i++];
      }
    }
    return min == Integer.MAX_VALUE ? 0 : min;
  }
}