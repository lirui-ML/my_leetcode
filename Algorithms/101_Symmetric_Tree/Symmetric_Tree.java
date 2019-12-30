import java.util.Queue;

/*
描述：对称二叉树
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
*/
public class TreeNode{
	int val;
	TreeNode left;
	TreeNode right;
	TreeNode(int x){
		this.val = x;
	}
}

class Solution{
	//递归
	public boolean isSymmetric(TreeNode root) {
		return isMirror(root, root);
	}
	
	public boolean isMirror(TreeNode t1,TreeNode t2) {
		if(t1 == null && t2 == null) return true;
		if(t1 == null || t2 == null) return false;
		if(t1.val == t2.val) {
			boolean outpair = isMirror(t1.left, t2.right);
			boolean inpair = isMirror(t1.right, t2.left);
			return outpair && inpair;
		}else {
			return false;
		}
	}
	// 迭代
	public boolean isSymmetric_2(TreeNode root) {
		Queue<TreeNode> q = new LinkedList<>();
		q.add(root);
		q.add(root);
		while(!q.isEmpty()) {
			TreeNode t1 = q.poll();
	        TreeNode t2 = q.poll();
	        if (t1 == null && t2 == null) continue;
	        if (t1 == null || t2 == null) return false;
	        if (t1.val != t2.val) return false;
	        q.add(t1.left);
	        q.add(t2.right);
	        q.add(t1.right);
	        q.add(t2.left);
		}
		return true;
	}
}