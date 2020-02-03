import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

/*
描述：二叉树的中序遍历，难度（medium）
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
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
    public List <Integer> inorderTraversal(TreeNode root) {
        //递归
    	List<Integer> res = new ArrayList <>();
        helper(root, res);
        return res;
    }

    private void helper(TreeNode root, List < Integer > res) {
        if (root != null) {
            if (root.left != null) {
                helper(root.left, res);
            }
            res.add(root.val);
            if (root.right != null) {
                helper(root.right, res);
            }
        }
    }
    
    public List <Integer> inorderTraversal_2(TreeNode root) {
    	//迭代
    	List<Integer> result = new ArrayList<>();
    	Stack<TreeNode> stack = new Stack<TreeNode>();
    	TreeNode curr = root;
    	while (curr != null || !stack.isEmpty()) {
    		while(curr != null) {
    			stack.push(curr);
    			curr = curr.left;
    		}
    		curr = stack.pop();
    		result.add(curr.val);
    		curr = curr.right;
    	}
    	return result;
    }
}
