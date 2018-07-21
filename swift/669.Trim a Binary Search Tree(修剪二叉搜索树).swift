/*
<p>
Given a binary search tree and the lowest and highest boundaries as <code>L</code> and <code>R</code>, trim the tree so that all its elements lies in <code>[L, R]</code> (R >= L). You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> 
    1
   / \
  0   2

  L = 1
  R = 2

<b>Output:</b> 
    1
      \
       2
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> 
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

<b>Output:</b> 
      3
     / 
   2   
  /
 1
</pre>
</p><p>给定一个二叉搜索树，同时给定最小边界<code>L</code>&nbsp;和最大边界&nbsp;<code>R</code>。通过修剪二叉搜索树，使得所有节点的值在<code>[L, R]</code>中 (R&gt;=L) 。你可能需要改变树的根节点，所以结果应当返回修剪好的二叉搜索树的新的根节点。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> 
    1
   / \
  0   2

  L = 1
  R = 2

<strong>输出:</strong> 
    1
      \
       2
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> 
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

<strong>输出:</strong> 
      3
     / 
   2   
  /
 1
</pre>
<p>给定一个二叉搜索树，同时给定最小边界<code>L</code>&nbsp;和最大边界&nbsp;<code>R</code>。通过修剪二叉搜索树，使得所有节点的值在<code>[L, R]</code>中 (R&gt;=L) 。你可能需要改变树的根节点，所以结果应当返回修剪好的二叉搜索树的新的根节点。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> 
    1
   / \
  0   2

  L = 1
  R = 2

<strong>输出:</strong> 
    1
      \
       2
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> 
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

<strong>输出:</strong> 
      3
     / 
   2   
  /
 1
</pre>
*/


/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.left = nil
 *         self.right = nil
 *     }
 * }
 */
class Solution {
    func trimBST(_ root: TreeNode?, _ L: Int, _ R: Int) -> TreeNode? {
        
    }
}