/*
�������������������еĽڵ㣬�Ѷȣ�medium��
����һ���������������������ڵĽڵ㣬�����ؽ����������

�㲻��ֻ�ǵ����ĸı�ڵ��ڲ���ֵ��������Ҫʵ�ʵĽ��нڵ㽻����

ʾ��:

���� 1->2->3->4, ��Ӧ�÷��� 2->1->4->3.

��Դ�����ۣ�LeetCode��
���ӣ�https://leetcode-cn.com/problems/swap-nodes-in-pairs
����Ȩ������������С���ҵת������ϵ�ٷ���Ȩ������ҵת����ע��������
*/

public class ListNode{
	int val;
	ListNode next;
	ListNode(int x){val = x;}
}

class Solution {
    public ListNode swapPairs(ListNode head) {

        // Dummy node acts as the prevNode for the head node
        // of the list and hence stores pointer to the head node.
        ListNode dummy = new ListNode(-1);
        dummy.next = head;

        ListNode prevNode = dummy;

        while ((head != null) && (head.next != null)) {

            // Nodes to be swapped
            ListNode firstNode = head;
            ListNode secondNode = head.next;

            // Swapping
            prevNode.next = secondNode;
            firstNode.next = secondNode.next;
            secondNode.next = firstNode;

            // Reinitializing the head and prevNode for next swap
            prevNode = firstNode;
            head = firstNode.next; // jump
        }

        // Return the new head node.
        return dummy.next;
    }
}