import javafx.util.Pair;
import java.lang.Math;
import java.util.LinkedList;
import java.util.Queue;

import javax.swing.tree.TreeNode;

import com.sun.org.apache.regexp.internal.recompile;

public class Maximum_Depth_of_Binary_Tree{
	public static void main(String[] args) {
		System.out.println();
	}
}

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution{
	public int maxDepth(TreeNode root) {
		/*
		 * 递归法 DFS
		 */
		if (root == null) {
			return 0;
		} else {
			int left_height = maxDepth(root.left);
			int right_height = maxDepth(root.right);
			return java.lang.Math.max(left_height, right_height) + 1;
	    }
	}
	
	public int maxDepth_3(TreeNode root) {
		/*
		 * 递归法
		 */
		if(root == null) {
			return 0;
		}
		return 1 + Math.max(maxDepth_3(root.left), maxDepth_3(root.right));
	}
	
	public int maxDepth_2(TreeNode root) {
		/*
		 * 迭代法 DFS
		 */
		Queue<Pair<TreeNode, Integer>> stack = new LinkedList<>();
		if(root != null) {
			stack.add(new Pair(root, 1));
		}
		int depth = 0;
		while (!stack.isEmpty()) {
			Pair<TreeNode, Integer> current = stack.poll();
			root = current.getKey();
			int current_depth = current.getValue();
			if (root != null) {
				depth = Math.max(depth, current_depth);
				stack.add(new Pair(root.left, current_depth + 1));
				stack.add(new Pair(root.right, current_depth + 1));
			}
		}
		return depth;
	}
}