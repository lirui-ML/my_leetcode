/*
描述：在排序数组中查找元素的第一个和最后一个位置，难度（medium）
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]

示例 2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
 */

class Solution {
  public int[] searchRange(int[] nums, int target) {
    //时间复杂度为O（logn），二分法
    int[] result = new int[] {-1, -1};
    if (nums == null || nums.length == 0){
      return result;
    }
    int left = 0, right = nums.length - 1;
    while (left <= right) {
      int mid = left + (right - left) / 2;
      if (nums[mid] == target) {
        int temp_left = mid, temp_right = mid;
        while (temp_left >= 0 && nums[temp_left] == nums[mid]) {
          temp_left--;
        }
        while (temp_right < nums.length && nums[temp_right] == nums[mid]) {
          temp_right++;
        }
        result[0] = temp_left + 1;
        result[1] = temp_right - 1;
        return result;
      } else if (nums[mid] < target) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }
    return result;
  }
}