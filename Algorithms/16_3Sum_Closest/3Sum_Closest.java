import java.util.Arrays;

/*
 * 标签：排序和双指针
 * 本题目因为要计算三个数，如果靠暴力枚举的话时间复杂度会到 O(n^3)，需要降低时间复杂度
 * 首先进行数组排序，时间复杂度 O(nlogn)
 * 在数组 nums 中，进行遍历，每遍历一个值利用其下标i，形成一个固定值 nums[i]
 * 再使用前指针指向 start = i + 1 处，后指针指向 end = nums.length - 1 处，也就是结尾处
 * 根据 sum = nums[i] + nums[start] + nums[end] 的结果，判断 sum 与目标 target 的距离，如果更近则更新结果 ans
 * 同时判断 sum 与 target 的大小关系，因为数组有序，如果 sum > target 则 end--，如果 sum < target 则 start++，
      如果 sum == target 则说明距离为 0 直接返回结果
 * 整个遍历过程，固定值为 n 次，双指针为 n 次，时间复杂度为 O(n^2)
 * 总时间复杂度：O(nlogn) + O(n^2) = O(n^2)
 */

class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int result = nums[0] + nums[1] + nums[2];
        
        for(int i = 0;i < nums.length; i++) {
        	int left = i + 1;
        	int right = nums.length - 1;
        	while(left < right) {
        		int sum = nums[i] + nums[left] + nums[right];
        		if (Math.abs(target - sum) < Math.abs(target - result))
        			result = sum;
        		if(sum < target)
        			left++;
        		else if(sum > target)
        			right--;
        		else
        			return target;
        	}
        }
        return result;
    }
}