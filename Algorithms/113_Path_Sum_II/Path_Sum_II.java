import java.util.ArrayList;
import java.util.List;

/*
描述：路径总和 II
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]
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
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
    	List<List<Integer>> result = new ArrayList<>();
    	List<Integer> path = new ArrayList<>();
    	dfs(root, sum, result, path);
    	return result;
    	
    }
    public void dfs(TreeNode root, int sum, List<List<Integer>> res, List<Integer> path) {
    	if(root == null) return;
    	path.add(root.val);
    	
    	if(root.left == null && root.right == null) {
    		if(root.val == sum) {
    			res.add(new ArrayList<Integer>(path));
    		}
    		return;
    	}
    	if(root.left != null) {
    		dfs(root.left, sum - root.val, res, path);
    		path.remove(path.size() - 1);
    	}
    	if(root.right != null) {
    		dfs(root.right, sum - root.val, res, path);
    		path.remove(path.size() - 1);
    	}
    }
}