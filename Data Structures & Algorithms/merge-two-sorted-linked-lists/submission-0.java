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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        // Traverse the list 
        // Increment if the list makes sense; 
        ListNode cur1 = list1;
        ListNode cur2 = list2;
        ListNode merge = new ListNode(0);
        ListNode rest = merge;

        while(cur1 != null && cur2 != null) {
            if (cur1.val > cur2.val) {
                rest.next = cur2;
                cur2 = cur2.next;
                rest = rest.next;
            }
            else {
                rest.next = cur1;
                cur1 = cur1.next;
                rest = rest.next;

            }
        }

        while(cur1 != null && cur2 == null) {
            rest.next = cur1;
            cur1 = cur1.next;
            rest = rest.next;

        }

        while(cur2 != null && cur1 == null) {
            rest.next = cur2;
            cur2 = cur2.next;
            rest = rest.next;
        }

        return merge.next;    
    }
}