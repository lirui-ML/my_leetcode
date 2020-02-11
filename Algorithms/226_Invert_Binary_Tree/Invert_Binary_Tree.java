import java.util.LinkedList;
import java.util.Queue;

/*
��������ת���������Ѷȣ�easy��
��תһ�ö�������

ʾ����

���룺
     4
   /   \
  2     7
 / \   / \
1   3 6   9
�����
     4
   /   \
  7     2
 / \   / \
9   6 3   1

��Դ�����ۣ�LeetCode��
���ӣ�https://leetcode-cn.com/problems/invert-binary-tree
����Ȩ������������С���ҵת������ϵ�ٷ���Ȩ������ҵת����ע��������
*/

/**
 * Definition for a binary tree node.
 */
 public class TreeNode {
	 int val;
	 TreeNode left;
	 TreeNode right;
   TreeNode(int x) { val = x; }
}
 
class Solution {
    public TreeNode invertTree(TreeNode root) {
      //�ݹ�
      helper(root);
      return root;
    }
    
    private void helper(TreeNode node) {
      if (node == null) {
        return;
        }
      if (node.left == null && node.right == null) {
        return;
        }
      if (node.left != null){
        TreeNode tmp = node.left;
        node.left = node.right;
        node.right = tmp;
        }else if (node.right != null) {
          TreeNode tmp = node.right;
          node.right = node.left;
          node.left = tmp;
        }
        helper(node.left);
        helper(node.right);
    }
    
    public TreeNode invertTree_2(TreeNode root) {
      //����
      if (root == null) {
        return null;
      }
      Queue<TreeNode> queue = new LinkedList<TreeNode>();
      queue.add(root);
      while (!queue.isEmpty()) {
        TreeNode curr = queue.poll();
        TreeNode tmp = curr.left;
        curr.left = curr.right;
        curr.right = tmp;
        if (curr.left != null)
          queue.add(curr.left);
        if (curr.right != null)
          queue.add(curr.right);
      }
      return root;
    }
}