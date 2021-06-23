#题目：合并两个有序链表 https://leetcode-cn.com/problems/merge-two-sorted-lists/ 
#题解：
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #思路：遍历，新开链表，谁小放谁
        #细节：未遍历完的链接，剩余部分之间追加
        Linked = ListNode()
        head = Linked
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                Linked.next = l1
                l1 = l1.next
            else:
                Linked.next = l2
                l2 = l2.next
            Linked = Linked.next
        if l1 == None:
            Linked.next = l2
        else:
            Linked.next = l1
        return head.next