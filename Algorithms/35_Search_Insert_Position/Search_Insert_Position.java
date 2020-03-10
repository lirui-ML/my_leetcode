/*
描述：搜索插入位置，难度（easy）
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
示例 3:

输入: [1,3,5,6], 7
输出: 4
示例 4:

输入: [1,3,5,6], 0
输出: 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-insert-position
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
 */

class Solution {
  public int searchInsert(int[] nums, int target) {
    //二分法，O（logn）时间复杂度
    int left = 0, right = nums.length - 1;
    while (left <= right){
      int mid = left + (right - left) / 2;
      if (nums[mid] == target){
        return mid;
      }else if (nums[mid] < target) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }
    return left;
  }
  public int searchInsert_2(int[] nums, int target) {
    //暴力求解，O（n）时间复杂度
    if (nums[0] > target) {
      return 0;
    }
    if (nums[nums.length - 1] < target) {
      return nums.length;
    }
    for (int i = 0;i < nums.length;i++) {
      if (nums[i] == target) {
        return i;
      } else if (nums[i] < target && nums[i + 1] > target) {
        return i + 1;
      }
    }
    return 0;
  }
}