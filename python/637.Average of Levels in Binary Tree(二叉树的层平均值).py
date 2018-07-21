"""
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b>
    3
   / \
  9  20
    /  \
   15   7
<b>Output:</b> [3, 14.5, 11]
<b>Explanation:</b>
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The range of node's value is in the range of 32-bit signed integer.</li>
</ol>
</p><p>给定一个非空二叉树, 返回一个由每层节点平均值组成的数组.</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong>
    3
   / \
  9  20
    /  \
   15   7
<strong>输出:</strong> [3, 14.5, 11]
<strong>解释:</strong>
第0层的平均值是 3,  第1层是 14.5, 第2层是 11. 因此返回 [3, 14.5, 11].
</pre>

<p><strong>注意：</strong></p>

<ol>
	<li>节点值的范围在32位有符号整数范围内。</li>
</ol>
<p>给定一个非空二叉树, 返回一个由每层节点平均值组成的数组.</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong>
    3
   / \
  9  20
    /  \
   15   7
<strong>输出:</strong> [3, 14.5, 11]
<strong>解释:</strong>
第0层的平均值是 3,  第1层是 14.5, 第2层是 11. 因此返回 [3, 14.5, 11].
</pre>

<p><strong>注意：</strong></p>

<ol>
	<li>节点值的范围在32位有符号整数范围内。</li>
</ol>
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        