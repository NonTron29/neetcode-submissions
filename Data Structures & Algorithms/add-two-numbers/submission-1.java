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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode cur1 = l1;
        ListNode cur2 = l2;
        int carry = 0;

        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;

        while (l1 != null || l2 != null || carry != 0) {
            int value = carry;

            if (l1 != null) {
                value += l1.val;
                l1 = l1.next;
            }

            if (l2 != null) {
                value += l2.val;
                l2 = l2.next;
            }

            cur.next = new ListNode(value % 10);
            cur = cur.next;
            carry = value / 10;
        }

        return dummy.next;
    }
}
