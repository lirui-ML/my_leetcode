import java.util.HashSet;
import java.util.Set;

/*
描述：缺失的第一个正数，难度（hard）
给定一个未排序的整数数组，找出其中没有出现的最小的正整数。

示例 1:
输入: [1,2,0]
输出: 3

示例 2:
输入: [3,4,-1,1]
输出: 2

示例 3:
输入: [7,8,9,11,12]
输出: 1

说明:
你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/first-missing-positive
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/

class Solution {
    public int firstMissingPositive(int[] nums) {
        int size = nums.length;
        for(int i = 0;i < size; i++) {
        	while(nums[i] > 0 && nums[i] <= size && nums[i] != nums[nums[i] - 1]) {
        		swap(nums, nums[i] - 1, i);
        	}
        }
        for(int i = 0;i < size;i++) {
        	if(nums[i] != i + 1) {
        		return i + 1;
        	}
        }
        return size + 1;
    }
    
    public void swap(int[] nums, int index1, int index2) {
    	int temp = nums[index1];
    	nums[index1] = nums[index2];
    	nums[index2] = temp;
    }
    
    public int firstMissingPositive2(int[] nums) {
    	int size = nums.length;
    	Set<Integer> hashset = new HashSet<>();
    	for(int num: nums) {
    		hashset.add(num);
    	}
    	for(int i = 1;i <= size; i++) {
    		if(!hashset.contains(i))
    			return i;
    	}
    	return size + 1;
    }
}