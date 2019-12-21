
public class contain_with_most_water{
	public static void main(String[] args) {
		Solution ss = new Solution();
		int[] sample = {1,8,6,2,5,4,8,3,7};
		int res  = ss.maxArea(sample);
		int res2 = ss.maxArea_2(sample);
		
		System.out.println("result is :"+res);
		System.out.println("result 2 is :"+res2);
	}
}

class Solution{
	public int maxArea(int[] height) {
		/*
		 * 暴力解法, 时间复杂度O(n^2)
		 */
		int maxarea = 0;
		for(int i = 0;i < height.length;++i) {
			for (int j = i + 1; j < height.length; j++) {
				maxarea = Math.max(maxarea, Math.min(height[i], height[j]) * (j - i));
			}
		}
		return maxarea;
	}
	
	public int maxArea_2(int[] height) {
		/*
		 * 双指针法，时间复杂度O(n)
		 */
		int maxarea = 0;
		int left = 0;
		int right = height.length - 1;
		while(left < right) {
			maxarea = Math.max(maxarea, Math.min(height[left], height[right]) * (right - left));
			
			if(height[left] < height[right]) {
				left++;
			}else {
				right--;
			}
		}
		return maxarea;
	}
}