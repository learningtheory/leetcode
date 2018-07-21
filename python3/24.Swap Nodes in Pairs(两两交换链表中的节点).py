"""
<p>Given a&nbsp;linked list, swap every two adjacent nodes and return its head.</p>

<p><strong>Example:</strong></p>

<pre>
Given <code>1-&gt;2-&gt;3-&gt;4</code>, you should return the list as <code>2-&gt;1-&gt;4-&gt;3</code>.</pre>

<p><strong>Note:</strong></p>

<ul>
	<li>Your algorithm should use only constant extra space.</li>
	<li>You may <strong>not</strong> modify the values in the list&#39;s nodes, only nodes itself may be changed.</li>
</ul>
<p>给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。</p>

<p><strong>示例:</strong></p>

<pre>给定 <code>1-&gt;2-&gt;3-&gt;4</code>, 你应该返回 <code>2-&gt;1-&gt;4-&gt;3</code>.</pre>

<p><strong>说明:</strong></p>

<ul>
	<li>你的算法只能使用常数的额外空间。</li>
	<li><strong>你不能只是单纯的改变节点内部的值</strong>，而是需要实际的进行节点交换。</li>
</ul>
<p>给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。</p>

<p><strong>示例:</strong></p>

<pre>给定 <code>1-&gt;2-&gt;3-&gt;4</code>, 你应该返回 <code>2-&gt;1-&gt;4-&gt;3</code>.</pre>

<p><strong>说明:</strong></p>

<ul>
	<li>你的算法只能使用常数的额外空间。</li>
	<li><strong>你不能只是单纯的改变节点内部的值</strong>，而是需要实际的进行节点交换。</li>
</ul>
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        