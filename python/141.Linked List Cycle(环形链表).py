"""
<p>
Given a linked list, determine if it has a cycle in it.
</p>

<p>
Follow up:<br />
Can you solve it without using extra space?
</p><p>给定一个链表，判断链表中是否有环。</p>

<p><strong>进阶：</strong><br>
你能否不使用额外空间解决此题？</p>
<p>给定一个链表，判断链表中是否有环。</p>

<p><strong>进阶：</strong><br>
你能否不使用额外空间解决此题？</p>
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        