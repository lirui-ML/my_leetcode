/*
�������ƶ��㣬�Ѷȣ�easy��
����һ������ nums����дһ������������ 0 �ƶ��������ĩβ��ͬʱ���ַ���Ԫ�ص����˳��

ʾ��:

����: [0,1,0,3,12]
���: [1,3,12,0,0]
˵��:

������ԭ�����ϲ��������ܿ�����������顣
�������ٲ���������

��Դ�����ۣ�LeetCode��
���ӣ�https://leetcode-cn.com/problems/move-zeroes
����Ȩ������������С���ҵת������ϵ�ٷ���Ȩ������ҵת����ע��������
*/

class Solution {
    public void moveZeroes(int[] nums) {
        if (nums == null || nums.length == 0) {
          return;
        }
        int n = nums.length;
        for (int i = 0; i < n; i++) {
          if (nums[i] != 0)
            continue;
          else {
            int tmp = i;
            while (tmp < n) {
              if (nums[tmp] == 0)
                tmp++;
              else {
                int data = nums[i];
                nums[i] = nums[tmp];
                nums[tmp] = data;
                break;
              }
            }
          }
        }
    }
    
    public void moveZeroes(int[] nums) {
      if (nums == null || nums.length == 0) 
        return;
      int n = nums.length;
      int p = 0;
      for (int i = 0; i < n; i++) {
        if (nums[i] != 0) {
          int tmp = nums[i];
          nums[i] = nums[p];
          nums[p] = tmp;
          p++;
          }
        }
    }
}