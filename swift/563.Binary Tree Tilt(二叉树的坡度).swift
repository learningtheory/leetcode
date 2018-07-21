/*
<p>Given a binary tree, return the tilt of the <b>whole tree</b>.</p>

<p>The tilt of a <b>tree node</b> is defined as the <b>absolute difference</b> between the sum of all left subtree node values and the sum of all right subtree node values. Null node has tilt 0.</p>

<p>The tilt of the <b>whole tree</b> is defined as the sum of all nodes' tilt.</p>

<p><b>Example:</b><br />
<pre>
<b>Input:</b> 
         1
       /   \
      2     3
<b>Output:</b> 1
<b>Explanation:</b> 
Tilt of node 2 : 0
Tilt of node 3 : 0
Tilt of node 1 : |2-3| = 1
Tilt of binary tree : 0 + 0 + 1 = 1
</pre>
</p>

<p><b>Note:</b>
<ol>
<li>The sum of node values in any subtree won't exceed the range of 32-bit integer. </li>
<li>All the tilt values won't exceed the range of 32-bit integer.</li>
</ol>
</p><p>给定一个二叉树，计算<strong>整个树</strong>的坡度。</p>

<p>一个树的<strong>节点的坡度</strong>定义即为，该节点左子树的结点之和和右子树结点之和的<strong>差的绝对值</strong>。空结点的的坡度是0。</p>

<p><strong>整个树</strong>的坡度就是其所有节点的坡度之和。</p>

<p><strong>示例:</strong></p>

<pre>
<strong>输入:</strong> 
         1
       /   \
      2     3
<strong>输出:</strong> 1
<strong>解释:</strong> 
结点的坡度 2 : 0
结点的坡度 3 : 0
结点的坡度 1 : |2-3| = 1
树的坡度 : 0 + 0 + 1 = 1
</pre>

<p><strong>注意:</strong></p>

<ol>
	<li>任何子树的结点的和不会超过32位整数的范围。</li>
	<li>坡度的值不会超过32位整数的范围。</li>
</ol>
<p>给定一个二叉树，计算<strong>整个树</strong>的坡度。</p>

<p>一个树的<strong>节点的坡度</strong>定义即为，该节点左子树的结点之和和右子树结点之和的<strong>差的绝对值</strong>。空结点的的坡度是0。</p>

<p><strong>整个树</strong>的坡度就是其所有节点的坡度之和。</p>

<p><strong>示例:</strong></p>

<pre>
<strong>输入:</strong> 
         1
       /   \
      2     3
<strong>输出:</strong> 1
<strong>解释:</strong> 
结点的坡度 2 : 0
结点的坡度 3 : 0
结点的坡度 1 : |2-3| = 1
树的坡度 : 0 + 0 + 1 = 1
</pre>

<p><strong>注意:</strong></p>

<ol>
	<li>任何子树的结点的和不会超过32位整数的范围。</li>
	<li>坡度的值不会超过32位整数的范围。</li>
</ol>
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
    func findTilt(_ root: TreeNode?) -> Int {
        
    }
}