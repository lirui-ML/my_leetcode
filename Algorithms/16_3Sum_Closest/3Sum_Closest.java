import java.util.Arrays;

/*
 * ��ǩ�������˫ָ��
 * ����Ŀ��ΪҪ���������������������ö�ٵĻ�ʱ�临�ӶȻᵽ O(n^3)����Ҫ����ʱ�临�Ӷ�
 * ���Ƚ�����������ʱ�临�Ӷ� O(nlogn)
 * ������ nums �У����б�����ÿ����һ��ֵ�������±�i���γ�һ���̶�ֵ nums[i]
 * ��ʹ��ǰָ��ָ�� start = i + 1 ������ָ��ָ�� end = nums.length - 1 ����Ҳ���ǽ�β��
 * ���� sum = nums[i] + nums[start] + nums[end] �Ľ�����ж� sum ��Ŀ�� target �ľ��룬�����������½�� ans
 * ͬʱ�ж� sum �� target �Ĵ�С��ϵ����Ϊ����������� sum > target �� end--����� sum < target �� start++��
      ��� sum == target ��˵������Ϊ 0 ֱ�ӷ��ؽ��
 * �����������̣��̶�ֵΪ n �Σ�˫ָ��Ϊ n �Σ�ʱ�临�Ӷ�Ϊ O(n^2)
 * ��ʱ�临�Ӷȣ�O(nlogn) + O(n^2) = O(n^2)
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