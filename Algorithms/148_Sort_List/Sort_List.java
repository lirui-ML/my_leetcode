/*
描述：排序链表 （难度：medium）
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:

输入: 4->2->1->3
输出: 1->2->3->4
示例 2:

输入: -1->5->3->4->0
输出: -1->0->3->4->5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/

//Definition for singly-linked list.
class ListNode {
	int val;
    ListNode next;
    ListNode(int x) { 
    	val = x; 
    }
}

class Solution {
    public ListNode sortList(ListNode head) {
        if(head == null || head.next == null)
        	return head;
        //step 1. cut the list to two parts
        ListNode prev = null;
        ListNode slow = head;
        ListNode fast = head;
        while(fast != null && fast.next != null) {
        	prev = slow;
        	slow = slow.next;
        	fast = fast.next.next;
        }
        prev.next = null;
        //step 2. sort each half
        ListNode left = sortList(head);
        ListNode right = sortList(slow);
        //step 3. merge left and right
        return merge(left, right);
    }
    
    ListNode merge(ListNode h1, ListNode h2) {
    	ListNode l = new ListNode(0), p = l;
    	while(h1 != null && h2 != null) {
    		if(h1.val < h2.val) {
    			p.next = h1;
    			h1 = h1.next;
    		}else {
				p.next = h2;
				h2 = h2.next;
			}
    		p = p.next;
    	}
    	if(h1 != null)
    		p.next = h1;
    	if(h2 != null)
    		p.next = h2;
    	return l.next;
    }	
}
