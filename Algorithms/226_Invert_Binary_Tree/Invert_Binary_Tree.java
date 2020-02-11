import java.util.LinkedList;
import java.util.Queue;

/*
描述：翻转二叉树，难度（easy）
翻转一棵二叉树。

示例：

输入：
     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：
     4
   /   \
  7     2
 / \   / \
9   6 3   1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/invert-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
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
      //递归
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
      //迭代
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