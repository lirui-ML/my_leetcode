/*
������·���ܺ� III���Ѷȣ�easy��
����һ��������������ÿ����㶼�����һ������ֵ��

�ҳ�·���͵��ڸ�����ֵ��·��������

·������Ҫ�Ӹ��ڵ㿪ʼ��Ҳ����Ҫ��Ҷ�ӽڵ����������·��������������µģ�ֻ�ܴӸ��ڵ㵽�ӽڵ㣩��

������������1000���ڵ㣬�ҽڵ���ֵ��Χ�� [-1000000,1000000] ��������

ʾ����
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

���� 3���͵��� 8 ��·����:

1.  5 -> 3
2.  5 -> 2 -> 1
3.  -3 -> 11

��Դ�����ۣ�LeetCode��
���ӣ�https://leetcode-cn.com/problems/path-sum-iii
����Ȩ������������С���ҵת������ϵ�ٷ���Ȩ������ҵת����ע��������
*/

public class TreeNode{
  int val;
  TreeNode left;
  TreeNode right;
  TreeNode (int x) {val = x;}
}


class Solution{
  public int pathSum(TreeNode root, int sum) {
    if (root == null)
      return;
    
  }
}