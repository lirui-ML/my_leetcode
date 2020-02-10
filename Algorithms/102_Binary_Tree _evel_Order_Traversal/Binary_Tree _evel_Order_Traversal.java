import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

import javax.swing.tree.TreeNode;

/*
鎻忚堪锛氫簩鍙夋爲鐨勫眰娆￠亶鍘嗭紝闅惧害锛坢edium锛�
缁欏畾涓�涓簩鍙夋爲锛岃繑鍥炲叾鎸夊眰娆￠亶鍘嗙殑鑺傜偣鍊笺�� 锛堝嵆閫愬眰鍦帮紝浠庡乏鍒板彸璁块棶鎵�鏈夎妭鐐癸級銆�

渚嬪:
缁欏畾浜屽弶鏍�:聽[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
杩斿洖鍏跺眰娆￠亶鍘嗙粨鏋滐細
[
  [3],
  [9,20],
  [15,7]
]

鏉ユ簮锛氬姏鎵ｏ紙LeetCode锛�
閾炬帴锛歨ttps://leetcode-cn.com/problems/binary-tree-level-order-traversal
钁椾綔鏉冨綊棰嗘墸缃戠粶鎵�鏈夈�傚晢涓氳浆杞借鑱旂郴瀹樻柟鎺堟潈锛岄潪鍟嗕笟杞浇璇锋敞鏄庡嚭澶勩��
*/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
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
    		res.add(currLevel);
    	}
    	return res;
    }
}