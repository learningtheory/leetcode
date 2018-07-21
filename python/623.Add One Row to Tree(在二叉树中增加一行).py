"""
<p>Given the root of a binary tree, then value <code>v</code> and depth <code>d</code>, you need to add a row of nodes with value <code>v</code> at the given depth <code>d</code>. The root node is at depth 1. </p>

<p>The adding rule is: given a positive integer depth <code>d</code>, for each NOT null tree nodes <code>N</code> in depth <code>d-1</code>, create two tree nodes with value <code>v</code> as <code>N's</code> left subtree root and right subtree root. And <code>N's</code> <b>original left subtree</b> should be the left subtree of the new left subtree root, its <b>original right subtree</b> should be the right subtree of the new right subtree root. If depth <code>d</code> is 1 that means there is no depth d-1 at all, then create a tree node with value <b>v</b> as the new root of the whole original tree, and the original tree is the new root's left subtree.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> 
A binary tree as following:
       4
     /   \
    2     6
   / \   / 
  3   1 5   

<b>v = 1</b>

<b>d = 2</b>

<b>Output:</b> 
       4
      / \
     1   1
    /     \
   2       6
  / \     / 
 3   1   5   

</pre>
</p>


<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> 
A binary tree as following:
      4
     /   
    2    
   / \   
  3   1    

<b>v = 1</b>

<b>d = 3</b>

<b>Output:</b> 
      4
     /   
    2
   / \    
  1   1
 /     \  
3       1
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The given d is in range [1, maximum depth of the given tree + 1].</li>
<li>The given binary tree has at least one tree node.</li>
</ol>
</p><p>给定一个二叉树，根节点为第1层，深度为 1。在其第&nbsp;<code>d</code>&nbsp;层追加一行值为&nbsp;<code>v</code>&nbsp;的节点。</p>

<p>添加规则：给定一个深度值 <code>d</code> （正整数），针对深度为 <code>d-1</code> 层的每一<strong>非空</strong>节点 <code>N</code>，为 <code>N</code> 创建两个值为&nbsp;<code>v</code>&nbsp;的左子树和右子树。</p>

<p>将&nbsp;<code>N</code> 原先的左子树，连接为新节点&nbsp;<code>v</code> 的左子树；将&nbsp;<code>N</code> 原先的右子树，连接为新节点&nbsp;<code>v</code> 的右子树。</p>

<p>如果 <code>d</code> 的值为 1，深度 d - 1 不存在，则创建一个新的根节点 <code>v</code>，原先的整棵树将作为 <code>v</code> 的左子树。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> 
二叉树如下所示:
       4
     /   \
    2     6
   / \   / 
  3   1 5   

<strong>v = 1</strong>

<strong>d = 2</strong>

<strong>输出:</strong> 
       4
      / \
     1   1
    /     \
   2       6
  / \     / 
 3   1   5   

</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> 
二叉树如下所示:
      4
     /   
    2    
   / \   
  3   1    

<strong>v = 1</strong>

<strong>d = 3</strong>

<strong>输出:</strong> 
      4
     /   
    2
   / \    
  1   1
 /     \  
3       1
</pre>

<p><strong>注意:</strong></p>

<ol>
	<li>输入的深度值 d 的范围是：[1，二叉树最大深度 + 1]。</li>
	<li>输入的二叉树至少有一个节点。</li>
</ol>
<p>给定一个二叉树，根节点为第1层，深度为 1。在其第&nbsp;<code>d</code>&nbsp;层追加一行值为&nbsp;<code>v</code>&nbsp;的节点。</p>

<p>添加规则：给定一个深度值 <code>d</code> （正整数），针对深度为 <code>d-1</code> 层的每一<strong>非空</strong>节点 <code>N</code>，为 <code>N</code> 创建两个值为&nbsp;<code>v</code>&nbsp;的左子树和右子树。</p>

<p>将&nbsp;<code>N</code> 原先的左子树，连接为新节点&nbsp;<code>v</code> 的左子树；将&nbsp;<code>N</code> 原先的右子树，连接为新节点&nbsp;<code>v</code> 的右子树。</p>

<p>如果 <code>d</code> 的值为 1，深度 d - 1 不存在，则创建一个新的根节点 <code>v</code>，原先的整棵树将作为 <code>v</code> 的左子树。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> 
二叉树如下所示:
       4
     /   \
    2     6
   / \   / 
  3   1 5   

<strong>v = 1</strong>

<strong>d = 2</strong>

<strong>输出:</strong> 
       4
      / \
     1   1
    /     \
   2       6
  / \     / 
 3   1   5   

</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> 
二叉树如下所示:
      4
     /   
    2    
   / \   
  3   1    

<strong>v = 1</strong>

<strong>d = 3</strong>

<strong>输出:</strong> 
      4
     /   
    2
   / \    
  1   1
 /     \  
3       1
</pre>

<p><strong>注意:</strong></p>

<ol>
	<li>输入的深度值 d 的范围是：[1，二叉树最大深度 + 1]。</li>
	<li>输入的二叉树至少有一个节点。</li>
</ol>
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        