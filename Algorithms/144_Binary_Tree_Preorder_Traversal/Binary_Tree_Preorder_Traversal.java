import java.util.LinkedList;
import java.util.List;;

/*
描述：二叉树的前序遍历，难度（medium）
给定一个二叉树，返回它的 前序 遍历。

 示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,2,3]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-preorder-traversal
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
    public List<Integer> preorderTraversal(TreeNode root) {
        //递归
    	List<Integer> result = new ArrayList<>();
        helper(root, result);
        return result;
    }
    private void helper(TreeNode node, List<Integer> res) {
    	if (node == null) {
    		return;
    	}
    	res.add(node.val);
    	helper(node.left, res);
    	helper(node.right, res);
    }
    
    public List<Integer> preorderTraversal_2(TreeNode root) {
    	//迭代
    	LinkedList<TreeNode> stack = new LinkedList<TreeNode>();
    	LinkedList<Integer> result = new LinkedList<Integer>();
    	if (root == null) {
    		return result;
		}
    	stack.add(root);
    	while (!stack.isEmpty()) {
    		TreeNode node = stack.pollLast();
    		result.add(node.val);
    		if (node.right != null) {
    			stack.add(node.right);
			}
    		if (node.left != null) {
    			stack.add(node.left);
    		}
    	}
    	return result;
    }
}