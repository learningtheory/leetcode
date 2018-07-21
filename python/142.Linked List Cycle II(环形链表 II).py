"""
<p>
Given a linked list, return the node where the cycle begins. If there is no cycle, return <code>null</code>.
</p>

<p>
<b>Note:</b> Do not modify the linked list.</p>

<p>
<b>Follow up</b>:<br>
Can you solve it without using extra space?
</p><p>给定一个链表，返回链表开始入环的第一个节点。&nbsp;如果链表无环，则返回&nbsp;<code>null</code>。</p>

<p><strong>说明：</strong>不允许修改给定的链表。</p>

<p><strong>进阶：</strong><br>
你是否可以不用额外空间解决此题？</p>
<p>给定一个链表，返回链表开始入环的第一个节点。&nbsp;如果链表无环，则返回&nbsp;<code>null</code>。</p>

<p><strong>说明：</strong>不允许修改给定的链表。</p>

<p><strong>进阶：</strong><br>
你是否可以不用额外空间解决此题？</p>
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        