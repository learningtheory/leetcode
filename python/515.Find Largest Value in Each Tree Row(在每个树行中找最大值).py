"""
<p>You need to find the largest value in each row of a binary tree.</p>

<p><b>Example:</b><br />
<pre>
<b>Input:</b> 

          1
         / \
        3   2
       / \   \  
      5   3   9 

<b>Output:</b> [1, 3, 9]
</pre>
</p>
<p>您需要在二叉树的每一行中找到最大的值。</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入:</strong> 

          1
         / \
        3   2
       / \   \  
      5   3   9 

<strong>输出:</strong> [1, 3, 9]
</pre>
<p>您需要在二叉树的每一行中找到最大的值。</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入:</strong> 

          1
         / \
        3   2
       / \   \  
      5   3   9 

<strong>输出:</strong> [1, 3, 9]
</pre>
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        