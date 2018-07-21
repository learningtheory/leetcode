"""
<p>Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

<b>Output:</b> True
</pre>
</p>


<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

<b>Output:</b> False
</pre>
</p>

<p>给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。</p>

<p><strong>案例 1:</strong></p>

<pre>
<strong>输入:</strong> 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

<strong>输出:</strong> True
</pre>

<p>&nbsp;</p>

<p><strong>案例 2:</strong></p>

<pre>
<strong>输入:</strong> 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

<strong>输出:</strong> False
</pre>

<p>&nbsp;</p>
<p>给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。</p>

<p><strong>案例 1:</strong></p>

<pre>
<strong>输入:</strong> 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

<strong>输出:</strong> True
</pre>

<p>&nbsp;</p>

<p><strong>案例 2:</strong></p>

<pre>
<strong>输入:</strong> 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

<strong>输出:</strong> False
</pre>

<p>&nbsp;</p>
"""


class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        