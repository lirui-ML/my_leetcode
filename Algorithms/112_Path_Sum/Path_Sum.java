import com.sun.org.apache.bcel.internal.generic.RETURN;

/*
描述：路径总和
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例: 
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
*/

public class Path_Sum{
	public static void main(String[] args){
		Solution ss = new Solution();


	}
}
class TreeNode{
	int val;
	TreeNode left;
	TreeNode right;
	TreeNode(int x) {
		// TODO Auto-generated constructor stub
		this.val = x;
	}
}

class Solution{
	public boolean hasPathSum(TreeNode root, int sum) {
		//递归
		if(root == null)return false;
		sum -= root.val;
		if((root.left == null && root.right == null)))
			return (sum == 0);
		return hasPathSum(root.left, sum) || hasPathSum(root.right, sum);
	}
	public boolean hasPathSum_2(TreeNode root, int sum) {
		//迭代
		if(root == null)
			return false;
		LinkedList<TreeNode> node_stack = new LinkedList();
		LinkedList<Integer> sum_stack = new LinkedList();
		node_stack.add(root);
		sum_stack.add(root.val);
		TreeNode node;
		int curr_sum;
		while (!node_stack.isEmpty()){
			node = node_stack.pollLast();
			curr_sum = sum_stack.pollLast();
			if((node.left == null) && (node.right == null) && (curr_sum == sum))
				return true;
			if(node.right != null){
				node_stack.add(node.right);
				sum_stack.add(curr_sum + node.right.val);
			}
			if(node.left != null){
				node_stack.add(node.left);
				sum_stack.add(curr_sum + node.left.val);
			}
		}
		return false;
	}
}