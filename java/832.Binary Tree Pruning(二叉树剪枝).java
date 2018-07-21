/**
<p>We are given the head node <code>root</code>&nbsp;of a binary tree, where additionally every node&#39;s value is either a 0 or a 1.</p>

<p>Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.</p>

<p>(Recall that the subtree of a node X is X, plus every node that is a descendant of X.)</p>

<pre>
<strong>Example 1:</strong>
<strong>Input:</strong> [1,null,0,0,1]
<strong>Output: </strong>[1,null,0,null,1]
 
<strong>Explanation:</strong> 
Only the red nodes satisfy the property &quot;every subtree not containing a 1&quot;.
The diagram on the right represents the answer.

<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_2.png" style="width:450px" />
</pre>

<pre>
<strong>Example 2:</strong>
<strong>Input:</strong> [1,0,1,0,0,0,1]
<strong>Output: </strong>[1,null,1,null,1]


<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_1.png" style="width:450px" />
</pre>

<pre>
<strong>Example 3:</strong>
<strong>Input:</strong> [1,1,0,1,1,0,1,0]
<strong>Output: </strong>[1,1,0,1,1,null,1]


<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/05/1028.png" style="width:450px" />
</pre>

<p><strong>Note: </strong></p>

<ul>
	<li>The binary tree&nbsp;will&nbsp;have&nbsp;at&nbsp;most <code>100 nodes</code>.</li>
	<li>The value of each node will only be <code>0</code> or <code>1</code>.</li>
</ul>
<p>给定二叉树根结点&nbsp;<code>root</code>&nbsp;，此外树的每个结点的值要么是 0，要么是 1。</p>

<p>返回移除了所有不包含 1 的子树的原二叉树。</p>

<p>( 节点 X 的子树为 X 本身，以及所有 X 的后代。)</p>

<pre>
<strong>示例1:</strong>
<strong>输入:</strong> [1,null,0,0,1]
<strong>输出: </strong>[1,null,0,null,1]
 
<strong>解释:</strong> 
只有红色节点满足条件&ldquo;所有不包含 1 的子树&rdquo;。
右图为返回的答案。

<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_2.png" style="width:450px" />
</pre>

<pre>
<strong>示例2:</strong>
<strong>输入:</strong> [1,0,1,0,0,0,1]
<strong>输出: </strong>[1,null,1,null,1]


<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_1.png" style="width:450px" />
</pre>

<pre>
<strong>示例3:</strong>
<strong>输入:</strong> [1,1,0,1,1,0,1,0]
<strong>输出: </strong>[1,1,0,1,1,null,1]


<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/05/1028.png" style="width:450px" />
</pre>

<p><strong>说明: </strong></p>

<ul>
	<li>给定的二叉树最多有&nbsp;<code>100</code>&nbsp;个节点。</li>
	<li>每个节点的值只会为&nbsp;<code>0</code> 或&nbsp;<code>1</code>&nbsp;。</li>
</ul>
<p>给定二叉树根结点&nbsp;<code>root</code>&nbsp;，此外树的每个结点的值要么是 0，要么是 1。</p>

<p>返回移除了所有不包含 1 的子树的原二叉树。</p>

<p>( 节点 X 的子树为 X 本身，以及所有 X 的后代。)</p>

<pre>
<strong>示例1:</strong>
<strong>输入:</strong> [1,null,0,0,1]
<strong>输出: </strong>[1,null,0,null,1]
 
<strong>解释:</strong> 
只有红色节点满足条件&ldquo;所有不包含 1 的子树&rdquo;。
右图为返回的答案。

<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_2.png" style="width:450px" />
</pre>

<pre>
<strong>示例2:</strong>
<strong>输入:</strong> [1,0,1,0,0,0,1]
<strong>输出: </strong>[1,null,1,null,1]


<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_1.png" style="width:450px" />
</pre>

<pre>
<strong>示例3:</strong>
<strong>输入:</strong> [1,1,0,1,1,0,1,0]
<strong>输出: </strong>[1,1,0,1,1,null,1]


<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/05/1028.png" style="width:450px" />
</pre>

<p><strong>说明: </strong></p>

<ul>
	<li>给定的二叉树最多有&nbsp;<code>100</code>&nbsp;个节点。</li>
	<li>每个节点的值只会为&nbsp;<code>0</code> 或&nbsp;<code>1</code>&nbsp;。</li>
</ul>
**/


/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode pruneTree(TreeNode root) {
        
    }
}