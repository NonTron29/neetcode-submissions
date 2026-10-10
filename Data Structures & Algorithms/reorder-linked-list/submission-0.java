/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public void reorderList(ListNode head) {
        // traverse through and find the half way point
        // reverse the half way point
        ListNode slow = head;
        ListNode fast = head;

        while(fast.next != null && fast.next.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }

        ListNode prev = null;
        ListNode cur = slow.next;
        slow.next = null;

        while(cur != null){
            ListNode temp = cur.next;
            cur.next = prev;
            prev = cur;
            cur = temp;
        }

        ListNode top = head;
        ListNode bot = prev;
        while(prev != null){
            ListNode temp = top.next;
            ListNode temp2 = prev.next;
            top.next = prev;
            prev.next = temp;
            top = temp;
            prev = temp2;
        }
    }
}
