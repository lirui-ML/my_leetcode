import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
/*
二叉树的层次遍历 II（难度：easy）
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
 */
import
class Solution {
  public List<List<Integer>> levelOrderBottom(TreeNode root) {
    List<List<Integer>> res = new ArrayList<>();
    if (root == null) {
      return res;
    }
    Queue<TreeNode> q = new LinkedList<>();
    q.add(root);
    while (!q.isEmpty()) {
      int levelsize = q.size();
      List<Integer> currLevel = new ArrayList<>();
      for (int i = 0;i < levelsize;i++) {
        TreeNode currNode = q.poll();
        currLevel.add(currNode.val);
        if(currNode.left != null)
          q.add(currNode.left);
        if (currNode.right != null)
          q.add(currNode.right);
      }
      res.add(0, currLevel);
    }
    return res;
  }
}