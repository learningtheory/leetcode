/*
<p>Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a <b>full binary tree</b>, but some nodes are null. </p>

<p>The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the <code>null</code> nodes between the end-nodes are also counted into the length calculation.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

<b>Output:</b> 4
<b>Explanation:</b> The maximum width existing in the third level with the length 4 (5,3,null,9).
</pre>


<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> 

          1
         /  
        3    
       / \       
      5   3     

<b>Output:</b> 2
<b>Explanation:</b> The maximum width existing in the third level with the length 2 (5,3).
</pre>


<p><b>Example 3:</b><br />
<pre>
<b>Input:</b> 

          1
         / \
        3   2 
       /        
      5      

<b>Output:</b> 2
<b>Explanation:</b> The maximum width existing in the second level with the length 2 (3,2).
</pre>

<p><b>Example 4:</b><br />
<pre>
<b>Input:</b> 

          1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
<b>Output:</b> 8
<b>Explanation:</b>The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).


</pre>

<p><b>Note:</b>
Answer will in the range of 32-bit signed integer.
</p><p>给定一个二叉树，编写一个函数来获取这个树的最大宽度。树的宽度是所有层中的最大宽度。这个二叉树与<strong>满二叉树（full binary tree）</strong>结构相同，但一些节点为空。</p>

<p>每一层的宽度被定义为两个端点（该层最左和最右的非空节点，两端点间的<code>null</code>节点也计入长度）之间的长度。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

<strong>输出:</strong> 4
<strong>解释:</strong> 最大值出现在树的第 3 层，宽度为 4 (5,3,null,9)。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> 

          1
         /  
        3    
       / \       
      5   3     

<strong>输出:</strong> 2
<strong>解释:</strong> 最大值出现在树的第 3 层，宽度为 2 (5,3)。
</pre>

<p><strong>示例&nbsp;3:</strong></p>

<pre>
<strong>输入:</strong> 

          1
         / \
        3   2 
       /        
      5      

<strong>输出:</strong> 2
<strong>解释:</strong> 最大值出现在树的第 2 层，宽度为 2 (3,2)。
</pre>

<p><strong>示例 4:</strong></p>

<pre>
<strong>输入:</strong> 

          1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
<strong>输出:</strong> 8
<strong>解释:</strong> 最大值出现在树的第 4 层，宽度为 8 (6,null,null,null,null,null,null,7)。
</pre>

<p><strong>注意:</strong> 答案在32位有符号整数的表示范围内。</p>
<p>给定一个二叉树，编写一个函数来获取这个树的最大宽度。树的宽度是所有层中的最大宽度。这个二叉树与<strong>满二叉树（full binary tree）</strong>结构相同，但一些节点为空。</p>

<p>每一层的宽度被定义为两个端点（该层最左和最右的非空节点，两端点间的<code>null</code>节点也计入长度）之间的长度。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

<strong>输出:</strong> 4
<strong>解释:</strong> 最大值出现在树的第 3 层，宽度为 4 (5,3,null,9)。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> 

          1
         /  
        3    
       / \       
      5   3     

<strong>输出:</strong> 2
<strong>解释:</strong> 最大值出现在树的第 3 层，宽度为 2 (5,3)。
</pre>

<p><strong>示例&nbsp;3:</strong></p>

<pre>
<strong>输入:</strong> 

          1
         / \
        3   2 
       /        
      5      

<strong>输出:</strong> 2
<strong>解释:</strong> 最大值出现在树的第 2 层，宽度为 2 (3,2)。
</pre>

<p><strong>示例 4:</strong></p>

<pre>
<strong>输入:</strong> 

          1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
<strong>输出:</strong> 8
<strong>解释:</strong> 最大值出现在树的第 4 层，宽度为 8 (6,null,null,null,null,null,null,7)。
</pre>

<p><strong>注意:</strong> 答案在32位有符号整数的表示范围内。</p>
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
    func widthOfBinaryTree(_ root: TreeNode?) -> Int {
        
    }
}