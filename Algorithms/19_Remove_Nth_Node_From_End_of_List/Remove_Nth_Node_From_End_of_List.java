import java.util.List;

/*
描述：删除链表的倒数第N个节点 (难度：medium）
删除链表的倒数第N个节点
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/
//Definition for singly-linked list.

class ListNode {
	int val;
	ListNode next;
	ListNode(int x) { val = x; }
}

class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
    	//单次遍历,运用双指针,时间复杂度为 O(n), 空间复杂度 O(1)
    	ListNode newhead = new ListNode(0);
    	newhead.next = head;
    	ListNode P = newhead;
    	ListNode q = newhead;
    	// Advances first pointer so that the gap between first and second is n nodes apart
    	for(int i = 0;i < n;i++) {
    		q = q.next;
    	}
    	while(q.next != null) {
    		q = q.next;
    		P = P.next;
    	}
    	P.next = P.next.next;
    	return newhead.next;
    }
    
    public ListNode removeNthFromEnd2(ListNode head, int n) {
    	//两次遍历算法
    	ListNode dummy = new ListNode(0);
        dummy.next = head;
        int length  = 0;
        ListNode first = head;
        while (first != null) {
            length++;
            first = first.next;
        }
        length -= n;
        first = dummy;
        while (length > 0) {
            length--;
            first = first.next;
        }
        first.next = first.next.next;
        return dummy.next;
    }
}

public class Remove_Nth_Node_From_End_of_List{
	public static void main(String[] args) {
		System.out.println();
	}
}