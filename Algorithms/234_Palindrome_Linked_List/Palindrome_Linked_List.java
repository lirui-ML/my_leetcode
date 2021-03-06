import java.util.ArrayList;

/*
描述：回文链表
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/

/**
 * Definition for singly-linked list.
 */
 public class ListNode {
	 int val;
	 ListNode next;
     ListNode(int x) { val = x; }
}
 
class Solution {
    public boolean isPalindrome(ListNode head) {
        //
		if(head == null || head.next == null){
			return true;
	}
    	ArrayList<Integer> res = new ArrayList<Integer>();
    	while(head != null)
    		res.add(head.val);
    		head = head.next;
		int i = 0;
		int j = arr.size()-1;
    	while(i<j) {
			if(arr.get(i).compareTo(arr.get(j))!=0) {
				return false;
			}
			++i;
			--j;
		}
		return true;
    }
}