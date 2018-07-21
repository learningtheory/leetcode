"""
<p>
Given two non-empty binary trees <b>s</b> and <b>t</b>, check whether tree <b>t</b> has exactly the same structure and node values with a subtree of <b>s</b>. A subtree of <b>s</b> is a tree consists of a node in <b>s</b> and all of this node's descendants. The tree <b>s</b> could also be considered as a subtree of itself.
</p>

<p><b>Example 1:</b><br>

Given tree s:
<pre>
     3
    / \
   4   5
  / \
 1   2
</pre>
Given tree t:
<pre>
   4 
  / \
 1   2
</pre>
Return <b>true</b>, because t has the same structure and node values with a subtree of s.
</p>

<p><b>Example 2:</b><br>

Given tree s:
<pre>
     3
    / \
   4   5
  / \
 1   2
    /
   0
</pre>
Given tree t:
<pre>
   4
  / \
 1   2
</pre>
Return <b>false</b>.
</p><p>给定两个非空二叉树 <strong>s</strong> 和 <strong>t</strong>，检验&nbsp;<strong>s</strong> 中是否包含和 <strong>t</strong> 具有相同结构和节点值的子树。<strong>s</strong> 的一个子树包括 <strong>s</strong> 的一个节点和这个节点的所有子孙。<strong>s</strong> 也可以看做它自身的一棵子树。</p>

<p><strong>示例 1:</strong><br />
给定的树 s:</p>

<pre>
     3
    / \
   4   5
  / \
 1   2
</pre>

<p>给定的树 t：</p>

<pre>
   4 
  / \
 1   2
</pre>

<p>返回 <strong>true</strong>，因为 t 与 s 的一个子树拥有相同的结构和节点值。</p>

<p><strong>示例 2:</strong><br />
给定的树 s：</p>

<pre>
     3
    / \
   4   5
  / \
 1   2
    /
   0
</pre>

<p>给定的树 t：</p>

<pre>
   4
  / \
 1   2
</pre>

<p>返回 <strong>false</strong>。</p>
<p>给定两个非空二叉树 <strong>s</strong> 和 <strong>t</strong>，检验&nbsp;<strong>s</strong> 中是否包含和 <strong>t</strong> 具有相同结构和节点值的子树。<strong>s</strong> 的一个子树包括 <strong>s</strong> 的一个节点和这个节点的所有子孙。<strong>s</strong> 也可以看做它自身的一棵子树。</p>

<p><strong>示例 1:</strong><br />
给定的树 s:</p>

<pre>
     3
    / \
   4   5
  / \
 1   2
</pre>

<p>给定的树 t：</p>

<pre>
   4 
  / \
 1   2
</pre>

<p>返回 <strong>true</strong>，因为 t 与 s 的一个子树拥有相同的结构和节点值。</p>

<p><strong>示例 2:</strong><br />
给定的树 s：</p>

<pre>
     3
    / \
   4   5
  / \
 1   2
    /
   0
</pre>

<p>给定的树 t：</p>

<pre>
   4
  / \
 1   2
</pre>

<p>返回 <strong>false</strong>。</p>
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        